#include<bits/stdc++.h>
#include<string>
using namespace std;
template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }
#define traverse(container, it) \
  for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define         mp(x, y) make_pair(x, y)
#define         SIZE(c) (int)c.size()
#define         pb(x) push_back(x)
//#define       map<char,int>::iterator it;
#define         ff first
#define         ss second
#define         ll long long
#define         ld long double
#define         pii pair< int, int >
#define         psi pair< string, int >
#define         p(n) printf("%d\n",n)
#define         p64(n) printf("%lld\n",n)
#define         s(n) scanf("%d",&n)
#define         s64(n) scanf("%I64d",&n)
#define         rep(i,a,b) for(i=a;i<b;i++)
#define         MOD (1000000007LL)





////////////////////////////////////////////////////////


int main(){
	std::ios::sync_with_stdio(false);
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,k=1;
    cin>>t;
    int r,c,w;
    while(t--){
        cin>>r>>c>>w;

        ll ans = 0;
        int i;
        cout<<"Case #"<<k++<<": ";
        if(c==w)    {
            cout<<r*w<<endl;
            continue;
        }
        if(w==1)    {
            cout<<r*c<<endl;
            continue;

        }

        for(i=0;i<c;i+=w)   {
            if(i!=0)
                ans++;

        }

        if(i==c-1)  cout<<r*(ans+w-1)<<endl;
        else cout<<r*(ans+w)<<endl;

    }

return 0;
}



