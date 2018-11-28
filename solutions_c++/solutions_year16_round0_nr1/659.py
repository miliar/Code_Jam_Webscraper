#include <bits/stdc++.h>
using namespace std;

#define f(i,a)  for(int i=0;(i)<(a);++i)
#define fab(i,a,b) for (int i = (a); (i) < (b); ++i)
#define fba(i,a,b) for (int i = (b) - 1; (i) >= (a); --i)
#define fit(it,c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define all(c) (c).begin(),(c).end()


typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef unsigned int uint;
typedef char u8;
typedef vector <int> vi;
typedef pair <int, int> pii;

ll pr(int x){
    int A[10]={0},s=10;
    ll a=0,y;
    while(s){
        y=(++a)*x;
        while(y){
            if(!A[y%10]){
                A[y%10]=1;
                s--;
            }
            y/=10;
        }
    }
    return a*x;
}


int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    ll z;
    int T,t,n;
    cin>>T;
    f(t,T){
        cout<<"Case #"<<t+1<<": "; 
        cin>>n;
        if(!n)
            cout<<"INSOMNIA\n";
        else
            cout<<pr(n)<<"\n";
    }
    return 0;
}
