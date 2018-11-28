#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;
int n;
int d;
int type[10];
string data[10];
int times;
int cc;
int ans, acount;

struct Node{
    char ch;
    vector<Node*> child;
    Node(){ ch = '~'; }
    Node(char x){ ch = x; }
};

void insert(Node* root, string a){
    for (int i = 0; i < a.size(); i++){
        bool flag = false;
        for (int j = 0; j < root -> child.size(); j++)
            if (a[i] == root -> child[j] -> ch){
                root = root->child[j];
                flag = true;
                break;
            }
        if (!flag){
            cc++;
            root->child.push_back(new Node(a[i]));
            root = root->child[root->child.size() - 1];
        }
    }
}

bool count()
{
    cc = 0;
    for (int i =  0; i < d; i++)
    {
       Node * root = new Node;
       cc ++;
       for (int j = 0; j < n; j++)
       {
            if (type[j] == i)
                insert(root, data[j]);
       }
    }
    if (cc > ans)
    {
        acount = 0;
        ans = cc;
    }
    if (cc == ans)
    {
        acount ++;
    }
}
bool  check()
{
    int w[5];
    memset(w,false,sizeof(w));
    for (int i = 0; i < n; i++)
    {
        w[type[i]] = true;
    }
    for (int i = 0; i < d; i++)
    {
        if (!w[i]) return false;
    }
    return true;
}
int dfs(int depth)
{
    if (depth == n)
    {
        if (check())
            count();
        return 0;
    }
    else
    {
        for (int i = 0; i < d; i++)
        {
             type[depth] = i;
             dfs(depth+1);
        }
    }
}
int main()
{
    freopen("D-small-attempt1.in","r",stdin);
    freopen("D-small.out","w",stdout);
    cin >> times;
    for (int t = 0; t < times; t++){
        cin >> n >> d;
        for (int i = 0; i < n; i++)
        {
            cin >> data[i];
        }
        ans = 0;
        acount = 0;
        dfs(0);
        printf("Case #%d: %d %d\n",t+1,ans,acount);
    }
}
