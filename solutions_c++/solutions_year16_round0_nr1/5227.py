#include<bits/stdc++.h>
#define s(x) scanf("%d",&x)
#define ll long long
#define l(x) scanf("%I64d",&x)
#define cst int t; s(t); while(t--)
#define fr freopen("A-large.in", "r", stdin)
#define finp ios_base::sync_with_stdio(false)
#define pb push_back
#define pf printf
using namespace std;


int main()
{
    fr;
    freopen("out.txt", "w", stdout);
    int ct=0;
    cst{
        ll n;
        cin>>n;
        vector<ll> num(10, 0);
        ll cnt=0, i;
        for( i=1; cnt!=10 && i<1000000; i++){
           ll m=n*i;
           while(m>0){
                ll lst=m%10;
                if(num[lst]==0)
                    num[lst]++, cnt++;
                if(cnt==10)
                    break;
                m/=10;
           }
        }
        if(cnt==10)
        cout<<"Case #"<<++ct<<": "<<n*i-n<<endl;
        else
        cout<<"Case #"<<++ct<<": INSOMNIA"<<endl;

    }
    return 0;
}
