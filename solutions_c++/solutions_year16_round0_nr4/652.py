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


int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    int T,t,k,c,s,x;
    ll pos,j,p;
    cin>>T;
    f(t,T){
        cout<<"Case #"<<t+1<<": "; 
        cin>>k>>c>>s;
	if(s<1+(k-1)/c) {
		cout<<"IMPOSSIBLE\n";
	} else {
		x=k;
		j=0;
		while(x>=c){
			pos=0;
			p=1;
			f(i,c){
				pos+=j*p;
				j++;
				p*=k;
			}
			x-=c;
			cout<<1+pos<<" ";
		}
		if(x){
			pos=0;
			p=1;
			f(i,c){
				pos+=j*p;
				if(j<k-1){
					j++;
				}
				p*=k;
			}
			cout<<1+pos<<" ";
		}
		cout<<"\n";
	}
    }
    return 0;
}
