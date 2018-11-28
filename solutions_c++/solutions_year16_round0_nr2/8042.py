#include<bits/stdc++.h>
using namespace std;
string s, s1;
int len;
map<string, int> vis;

string flip(string ss, int upto)
{
    char cc[len+2];
    int j=0;
    
    for(int i=upto;i>=0;i--)
    {
        cc[j++] = ss[i] == '+' ? '-' : '+';
    }
    for(int i=upto+1;i<len;i++)
        cc[j++] = ss[i];
    cc[j] = '\0';
    
    string now = string(cc);
    return now;
}

int bfs()
{
    vis[s] = 1;
    queue<string> q;
    q.push(s);
    while(!q.empty())
    {
        string fr = q.front();
        q.pop();
        for(int i=0;i<len;i++)
        {
            string nxt = flip(fr, i);
            if(nxt==s1)
            {
                return vis[fr];
            }
            if(vis[nxt] == 0)
            {
                vis[nxt] = vis[fr] + 1;
                q.push(nxt);
            }
                
        }
    }
}
int main()
{
    //freopen("in.txt", "r", stdin);
    //freopen("b.txt", "w", stdout);
    int t, i, cas;
    cin>>t;
    for(cas=1;cas<=t;cas++)
    {
        cin>>s;
        len = s.size();
        char tem[len+2];
        for(i=0;i<len;i++)
        {
            tem[i] = '+';
        }
        tem[i] = '\0';
        
        s1 = string(tem);
        
        cout << "Case #" << cas << ": ";
        if(s==s1)
            cout << "0\n";
        else  cout << bfs() << "\n";
        vis.clear();
    }
    return 0;
}
