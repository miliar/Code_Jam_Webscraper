//
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define MOD 1000000007
#define INF 2147483647
#define PI 3.1415926535897932384626433832795
#define all(cont) cont.begin(),cont.end()
#define init(a,val) memset(a,val,sizeof(a))
#define F first
#define S second
#define mp make_pair
//GLOBAL
ll gcd(ll a,ll b)
{
    return b?gcd(b,a%b):a;
}
int main()
{
    freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
    int test_cases,Testno;

    ll cnt,p,q,k,l;
    cin>>test_cases;
    for(Testno=1;Testno<=test_cases;Testno++)
    {
        printf("Case #%d: ",Testno);
//___________________________________________
        scanf("%lld/%lld",&p,&q);
        cnt=0;
        k=gcd(p,q);
        l=q;
        q/=k;
        if(q&(q-1)){cout<<"impossible";goto Done;}
        while(p<l)
        {
            p*=2;
            cnt++;
        }
        if(cnt>40){cout<<"impossible";goto Done;}
        cout<<cnt;
//___________________________________________
        Done: printf("\n");
    }

return 0;
}
