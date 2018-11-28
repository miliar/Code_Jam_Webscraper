#include<bits/stdtr1c++.h>
using namespace std;

int dp[11][1<<12];
 vector<int> v,vis;
 int n,x;
int solve(int ind,int mask)
{
    
    if(ind==v.size())
        return 0;
    int &ret=dp[ind][mask];
    if(ret!=-1)
        return ret;
    if(mask & (1<<ind)) ret=solve(ind+1,mask);
    else
    {
            mask|=(1<<ind);
            ret=1+solve(ind+1,mask);
            for(int i=ind+1;i<v.size();i++)
            {
                if(v[i]+v[ind]<=x)
                {
                    ret=min(ret,1+solve(ind+1,mask|(1<<i)));
                }
            }
    }
    
    return ret;
}


int main()
{
    #ifndef ONLINE_JUDGE
        freopen("2.in","r",stdin);
        freopen("3.out","w",stdout);
        
    #endif // ONLINE_JUDGE
    
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int tc;
    cin>>tc;
   
    for(int ic=1;ic<=tc;ic++)
    {
        cin>>n>>x;
        v.clear();
        v.resize(n);
        for(int i=0;i<n;i++)
            cin>>v[i];
            
        sort(v.begin(),v.end());
        int ret=0;
        vis.clear();
        vis.resize(n,0);
        int i2=v.size()-1;
        int f=0;
        for(int i=0;i<v.size();i++)
        {
            if(vis[i])continue;
            ret++;
            int r=x-v[i];
            
            while(i2>=0 && v[i2]>r)
            {
                i2--;
            }
            if(i2>=0 && i2<v.size()&& v[i2]<=r)
                {
                    vis[i2--]=1;
                }
        }
        
        cout<<"Case #"<<ic<<": ";
        cout<<ret<<endl;
    
    }
    return 0;
    
}
