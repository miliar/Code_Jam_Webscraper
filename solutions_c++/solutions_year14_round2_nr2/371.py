#include<bits/stdtr1c++.h>
using namespace std;
#define Lower 1
#define Equal 0
#define Greater 2

typedef long long LL;

int a,b,k;
int cmp(int old,int n,int v,int ind)
{
    int bb=((n&(1<<ind))!=0);
    //cout<<n<<" "<<ind<<" "<<bb<<endl;
    if(old!=Equal) return old;
    if(v==bb) return Equal;
    if(v>bb) return Greater;
    return Lower;

}

LL dp[31][3][3][3];
LL solve(int ind,int cmpa,int cmpb,int cmpk)
{
    //cout<<ind<<endl;
    if(ind==-1)
    {
        return (cmpa==Lower && cmpb==Lower && cmpk==Lower);
    }
    
    LL &ret=dp[ind][cmpa][cmpb][cmpk];
    if(ret!=-1)
        return ret;
    
    ret=0;
    for(int i=0;i<=1;i++)
        for(int j=0;j<=1;j++)
        {
            ret+=solve(ind-1,cmp(cmpa,a,i,ind),cmp(cmpb,b,j,ind),cmp(cmpk,k,(i&j),ind));
        }
    
    //cout<<ind<<" "<<ret<<" "<<cmpa<<" "<<cmpb<<" "<<cmpk<<endl;
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
    
    int t;
    cin>>t;
    for(int ic=1;ic<=t;ic++)
    {
        cin>>a>>b>>k;

        cout<<"Case #"<<ic<<": ";
        memset(dp,-1,sizeof dp);
        cout<<solve(30,0,0,0)<<endl;
        
    }
    
    return 0;
    
}
