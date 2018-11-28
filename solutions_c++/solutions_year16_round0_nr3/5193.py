#include<iostream>
#include<vector>
#include<stack>
#include<queue>
using namespace std;
#define pb push_back
#define LL long long
#define FOR(i,m) for(i=1;i<=m;i++)
int array[100][100],m;
int level[1000];
int visited[1000]={0};
int dfs(int src);
main()
{
    while(cin>>m)
    {
        int i;
        for(int i=1;i<=m;i++)
        for(int j=1;j<=m;j++)
        cin>>array[i][j];
        level[1]=0;
        visited[1]=1;
        dfs(1);
        FOR(i,m)
       // for(int i=1;i<=m;i++)
        cout<<level[i]<<endl;

    }
}
int dfs(int src)
{
    for(int i=1;i<=m;i++)
    {
        int c=array[src][i];
        if(!visited[i] && c)
        {
            level[i]=level[src]+1;
            visited[i]=1;
            cout<<i<<endl;
            dfs(i);
        }
    }
}
