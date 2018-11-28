#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <deque>
#include <cmath>
#include <map>
#define mod 1000000007LL
using namespace std;

char a[10][10];


vector <int> list[30];
map <int,int> key;
map <int,int> ::iterator it;
vector <int> ans;
int unit[25];
int open[30];
int N;
bool mark[1024*1024*4];

void insert(int x)
{
    it=key.find(x);
    if(it==key.end())
        key.insert(make_pair(x,1));
    else it->second++;
}
void del(int x)
{
    it=key.find(x);
    if(it->second==1)
        key.erase(it);
    else it->second--;
}

void dfs(int state)
{
    mark[state]=true;
    int i,j;
    if(state==unit[N]-1)
    {
        for(i=0;i<ans.size();i++)
            cout<<" "<<ans[i]+1;
            cout<<endl;
        return;
    }
    if(mark[unit[N]-1]) return;
    
    for(i=0;i<N;i++)
    {
        if(unit[i]&state)//already open
            continue;
        it=key.find(open[i]);
        if(it==key.end())//no such key
            continue;
        if(mark[state+unit[i]])
            continue;
        
        
        ans.push_back(i);
        del(open[i]);
        for(j=0;j<list[i].size();j++)
            insert(list[i][j]);
        dfs(state+unit[i]);
        ans.pop_back();
        insert(open[i]);
        for(j=0;j<list[i].size();j++)
            del(list[i][j]);
        
    }
    
}


int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int re,K,i,m,x;
    cin>>re;
    
    unit[0]=1;
    for(i=1;i<25;i++)
    unit[i]=unit[i-1]*2;
    int cases=1;
    while(re--)
    {
        cin>>K>>N;
        for(i=0;i<N;i++)
            list[i].clear();
        key.clear();
        for(i=0;i<K;i++)//initial key
        {
            cin>>x;
            insert(x);   
        }
        for(i=0;i<N;i++)
        {
            cin>>open[i];
            cin>>m;
            while(m--)
            {
                cin>>x;
                list[i].push_back(x);
            }
        }
        
        memset(mark,0,sizeof(mark));
        
        printf("Case #%d:",cases++);
        ans.clear();
        dfs(0);
        
        if(!mark[unit[N]-1])
            cout<<" IMPOSSIBLE"<<endl;
        
    }
    return 0;
}
