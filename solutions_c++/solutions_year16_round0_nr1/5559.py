//__hr1212__//

#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef map<int,int> mi;

#define si(a) scanf("%lld",&a)
#define sii(a,b) scanf("%lld %lld",&a,&b)
#define nl printf("\n");
#define pi(a) printf("%lld\n",a)
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define f(i,a,b) for(i=a;i<b;i++)
#define rf(i,a,b) for(i=a;i>=b;i--)
#define clr(x,a) memset(x,a,sizeof(x))
#define MAX 10001
#define MOD 1000000007
#define F first
#define S second

ll n,m,a[MAX],b[MAX],mk[15];

int main(){
    ll r,k,i,c=0,x=0,y=0,j,t,l,z,x1=0,y1=0;
    ll ans=0;string p;

    si(t);
    f(j,1,t+1){

        si(n);
        clr(mk,0);
        printf("Case #%lld: ",j);
        f(i,1,MAX){
            x=n*i;
            while(x){
                mk[x%10]=1;
                x/=10;
            }
            c=0;
            f(l,0,10)
                if(mk[l])
                    c++;
            if(c==10)
                break;
        }
        if(i==MAX)
            cout<<"INSOMNIA";
        else
            cout<<n*i;
        nl;
    }

    return 0;
}
