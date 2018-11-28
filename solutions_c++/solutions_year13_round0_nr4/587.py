#include<iostream>
#include<cstring>
#include<map>
using namespace std;
struct box
{
    int key;
    int has[41];
}b[21];

int dp[1<<20];
bool vis[21];
int order[21];
int producer[41];
int consumer[41];
bool dfs(int re,int n,int st);
int main()
{
    int t,cas,k,n;
    cin>>cas;
    for(int q =1;q<=cas ; q++)
    {
        map<int,int> M;
        memset(dp,false,sizeof(dp));
        for(int j = 0 ;j < 20 ; j++)
            memset(b[j].has,false,sizeof(b[j].has));
        memset(producer,false,sizeof(producer));
        memset(consumer,false,sizeof(consumer));
        memset(vis,false,sizeof(vis));

        cin>>k>>n;
        for(int i= 0 ;i < k ; i++)
        {
            cin>>t;
            if(M.count(t)) t =M[t];
            else t = M[t] = M.size();
            producer[t]++;
        }
        for(int i = 0 ;i < n ; i++)
        {
            cin>>t;
            if(M.count(t)) t =M[t];
            else t = M[t] = M.size();
            b[i].key = t;
            consumer[ b[i].key ]++;

            cin>>t;
            for(int j = 0 ;j < t ; j++)
            {
                int t1;cin>>t1;
                if(M.count(t1)) t1 =M[t1];
                else t1 = M[t1] = M.size();

                b[i].has[t1]++;
            }
        }
        cout<<"Case #"<<q<<":";
        if(dfs(n,n,0))
        {
            for(int i = n ; i> 0 ;i--)
            {
                cout<<' '<<order[i]+1;
            }
            cout<<endl;
        }
        else cout<<" IMPOSSIBLE"<<endl;
    }
}
bool dfs(int re,int n,int state)
{
    if(dp[state] == -1)return false;
    if(re==0)
    {
        for(int i = 0 ;i<n;i++)
            if(!vis[i])return false;
        return true;
    }
    bool end = true;
    for(int i = 0 ;i < 40 ;i++)
        if(producer[i] < consumer[i])end = false;

    if(end)
    {
        for(int i = 0 ;i < n ; i++)
            if(!vis[i]) order[re--] = i;
          //  cout<<"Great !"<<endl;
        return true;
    }

    for(int i = 0 ;i < n ; i++)
    {
        int u = b[i].key;
        if( !vis[i] && producer[u])
        {
            vis[i] = true; producer[u]--;
            for(int j = 0 ;j < 40;j++)
                producer[j]+=b[i].has[j];
            order[re]=i;
            if(dfs(re-1,n,state | (1<<i) )) return true;

            for(int j = 0 ;j < 40;j++)
                producer[j]-=b[i].has[j];

            vis[i] = false;producer[u]++;
        }
    }
    dp[state] = -1;
    return false;
}
