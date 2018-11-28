#include <bits/stdc++.h>
using namespace std;
#define For(i,a,b) for(long long i=a;i<b;i++)
#define reset(a,b) memset(a,b,sizeof(a))
#define mod 1000000007
#define pi acos(-1)
#define eps 0.00000001
#define pb push_back

int t,n,lis[4][4],ori,ans,use[4],line[4],mac[4];
bool can;

void fromlis()
{
    int bas=1;
    For(i,0,n) For(j,0,n)
    {
        ori+=bas*lis[i][j];
        bas*=2;
    }
}
void tolis(int cp)
{
    For(i,0,n) For(j,0,n)
    {
        lis[i][j]=cp&1;
        cp/=2;
    }
}

bool test(int x)
{
    if(x==n) return true;
    bool found=false;
    int peo=line[x];
    For(i,0,n) if(!mac[i]&&lis[peo][i])
    {
        found=true;
        mac[i]=1;
        if(!test(x+1)) return false;
        mac[i]=0;
    }
    return found;
}

void fil(int x)
{
    if(x==n)
    {
        reset(mac,0);
        if(!test(0)) can=false;
        return;
    }
    For(i,0,n) if(!use[i])
    {
        use[i]=1;
        line[x]=i;
        fil(x+1);
        use[i]=0;
    }
}

bool pos()
{

    reset(use,0);
    can=true;
    fil(0);
    return can;
}

string s;

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ios::sync_with_stdio(0);
    cin>>t;
    For(cas,1,1+t)
    {
        cout<<"Case #"<<cas<<": ";
        cin>>n;
        ori=0;
        For(i,0,n)
        {
            cin>>s;
            For(j,0,n) if(s[j]=='0') lis[i][j]=0; else lis[i][j]=1;
        }
        fromlis();
        ans=mod;
        For(mask,1,1<<(n*n)) if((mask&ori)==ori)
        {
            tolis(mask);
            if(pos()) ans=min(ans,__builtin_popcount(mask^ori));
            //cout<<mask<<' '<<ans<<endl;
        }
        cout<<ans<<endl;
    }
}
