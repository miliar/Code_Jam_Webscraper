#include <iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
using namespace std;

int m,n,worst,ret;
vector<string> str;
int assign[10];

class node
{
    public:
        node* next[26];
};

node* r[10];


node* insert(node* root, string s)
{
    if (root == NULL)
    {
        root = new node;
        for (int i = 0; i < 26; i++)
            root->next[i] = NULL;
    }
    node *p = root;
    for (int i = 0; i < s.length(); i++)
    {
        if (root->next[s[i] - 'A'] == NULL)
        {
            node * tmp = new node;
            for (int j = 0; j < 26 ; j++)
                tmp->next[j] = NULL;
            root->next[s[i] - 'A'] = tmp;
            root = tmp;
        }
        else root = root->next[s[i] - 'A'];
    }
    return p;
}

int calc(node * r)
{
    if (r == NULL)
        return 0;
    int ans = 1;
    for (int i = 0; i < 26; i++)
        ans += calc(r->next[i]);
    return ans;
}

void del(node * r)
{
    if (r == NULL)
        return ;
    for (int i = 0; i < 26; i++)
        del(r->next[i]);
    delete r;
}

void brute(int index)
{
    if (index == m)
    {
        for (int i = 0; i < n; i++)
            r[i] = NULL;
        for (int i = 0; i < m; i++)
            r[assign[i]] = insert(r[assign[i]],str[i]);
        int number = 0;
        for (int i = 0; i < n; i++)
            number += calc(r[i]);
        if (number == worst)
            ret++;
        if (number > worst)
        {
            worst = number;
            ret = 1;
        }
        for (int i = 0; i < n; i++)
            del(r[i]);
    }
    else
    {
        for (int i = 0; i < n; i++)
        {
            assign[index] = i;
            brute(index + 1);
        }
    }
}
 
int main()
{
    int tt;
    cin >> tt;
    for (int ii = 0; ii < tt; ii++)
    {
        cin >> m >> n;
        ret = worst = 0;
        str.clear();
        for (int i = 0; i < m; i++)
        {
            string tmp;
            cin >> tmp;
            str.push_back(tmp);
        }
        brute(0);
        cout << "Case #" << ii + 1 << ": " << worst << ' ' << ret << endl;
    }
    return 0;
}
 
