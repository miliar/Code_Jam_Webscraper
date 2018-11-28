//__hr1212__//

#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<ll> vi;
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
#define MAX 100000100
#define MOD 1000000007
#define F first
#define S second

ll n,m,b[6000000],mk[18];

bool a[MAX];

vi v;

int main(){
    ll n1,n2,r,k,i,c=0,x=0,y=0,j,t,l,z,x1=0,y1=0,flag,p,q=0;
    ll ans=0;

    si(t);
    sii(n1,n2);

    k=0;
    f(i,2,MAX){
        if(!a[i]){
            b[k++]=i;
            for(j=2*i;j<MAX;j+=i){
                a[j]=1;
            }
        }
    }

     cout<<"Case #1:"<<endl;
    f(j,0,1<<14){
        c=j;r=j;
        l=0;
        clr(mk,0);
        while(c){
            mk[l]=c%2;
            c/=2;
            l++;
        }
        v.clear();
        f(x,2,11){
            ans=1;
            y=x;
            rf(i,13,0){
                if(mk[i])
                    ans+=y;
                y*=x;
            }
            ans+=y;

            flag=0;
            f(y,0,k){
                if(b[y]*b[y]>ans){
                    flag=1;
                    break;
                }
                else if(ans%b[y]==0){
                    v.pb(b[y]);
                    break;
                }
            }
            if(flag)
                break;
        }

        if(v.size()==9){
            cout<<1;
            f(i,0,14)
                cout<<mk[i];
            cout<<1<<" ";

            f(l,0,v.size())
                cout<<v[l]<<" ";
            nl;
            q++;
            if(q==50)
                break;
        }

    }

    return 0;
}
