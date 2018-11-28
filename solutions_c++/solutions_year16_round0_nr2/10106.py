#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<map>
#include<set>
#include<vector>
#include<queue>
#include<stack>
#include<bitset>
#include<sstream>
using namespace std;

string s;
map<string,int>visited;
map<string,int>level;
vector<char>v;
vector<char>r;

int bfs(string rr)
{

    queue<string>q;
    q.push(s);
    visited[s]=1;
    level[s]=0;
    int res=0;

    while(!q.empty()){
        string u=q.front();
        q.pop();
        if(u==rr){
            res=level[u];
            break;
        }
        for(int i=0;i<u.length();i++){
            for(int j=i;j>=0;j--){
                if(u[j]=='+')
                    v.push_back('-');
                else v.push_back('+');
            }

            for(int k=i+1;k<u.length();k++){
                v.push_back(u[k]);
            }
            string ss(v.begin(),v.end());
            if(visited[ss]==0){
                q.push(ss);
                visited[ss]=1;
                level[ss]=level[u]+1;
            }
            v.clear();

        }
    }
    return res;
}

int main()
{
    int t,tt=1;
    scanf("%d",&t);
    while(tt<=t){
        cin>>s;
        visited.clear();
        level.clear();
        for(int i=0;i<s.length();i++)
            r.push_back('+');
        string rr(r.begin(),r.end());
        int ans=bfs(rr);
        printf("Case #%d: %d\n",tt++,ans);
        r.clear();
    }
    return 0;
}
