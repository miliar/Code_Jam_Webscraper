#include <bits/stdc++.h>
using namespace std;

bool check(string s)
{
    for(int i = 0; i < s.size(); i++)
    {
        if(s[i] != '+')
            return false;
    }
    return true;
}

string halfflip(string s)
{
    if(s[0] == '-')
        s[0] = '+';
    else if(s[0] == '+')
        s[0] = '-';
    for(int i = 1; i < s.size();i++)
    {
        if(s[i] != s[i-1])
        {
            if(s[i] == '-')
                s[i] = '+';
            else if(s[i] == '+')
                s[i] = '-';
        }
        else
            break;
    }
    return s;
}

string fullflip(string s)
{
    for(int i = 0; i < s.size();i++)
    {
        if(s[i] == '-')
            s[i] = '+';
        else if(s[i] == '+')
            s[i] = '-';
    }
    for(int i = 0; i < s.size()/2; i++)
    {
        swap(s[i],s[s.size()-i-1]);
    }
    return s;
}

int main()
{
    int t;
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&t);
    //bfs
    queue <pair<string,int> > q;
    pair <string,int> p;
    for(int a = 1; a <= t; a++)
    {
        string s;
        cin >> s;
        q.push(make_pair(s,0));
        int x = 0;
        while(!q.empty())
        {
            p = q.front();
            q.pop();
            if(check(p.first))
                break;
            q.push(make_pair(halfflip(p.first),p.second+1));
            //printf("a");
            q.push(make_pair(fullflip(p.first),p.second+1));
            //printf("b");
            x++;
        }
        printf("Case #%d: %d\n",a,p.second);
        //clear queue
        while(!q.empty())
            q.pop();
    }
}
