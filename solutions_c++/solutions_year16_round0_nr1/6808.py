#include<bits/stdc++.h>
#define MOD 1000000007
#define len(a) strlen(a)
#define ll long long
#define nl printf("\n")
#define F first
#define S second
#define db printf("debug")
#define yes printf("YES\n")
#define no printf("NO\n")
#define pb(a) push_back(a)
#define po(a) pop_back()
#define mp(a,b) make_pair(a,b)
#define set(a,v) memset(a,v,sizeof(a))
#define sz(v) v.size()
#define gc getchar//_unlocked
#define pcase(i) printf("Case #%d: ",i)

using namespace std;

bool chk(vector<bool>flag)
{
    int i;
    for(i=0;i<=9;i++)
    {
        if(flag[i]==false)
            return false;
    }
    return true;
}
void set_flag(ll ans,vector<bool>&flag)
{
    int r;
    while(ans>0)
    {
        r=ans%10;
        ans= ans/10;
        flag[r]=true;
    }
    flag[r]=true;
}

int main()
{
    int t;
    scanf("%d",&t);
    for(int x=1;x<=t;x++)
    {
        pcase(x);
        vector<bool>flag(10,false);
        ll n,ans,k=1;
        cin>>n;
        ans=n;
        if(ans==0)
        {
            cout<<"INSOMNIA\n";
            continue;
        }
        set_flag(ans,flag);
        while(1)
        {
            ans=n*k;
            set_flag(ans,flag);
            if(chk(flag))
                break;
            k++;
        }
        cout<<ans;nl;
    }
}
