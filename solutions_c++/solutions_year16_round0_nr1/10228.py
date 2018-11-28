#include <bits/stdc++.h>
// Input macros
#define s(n)                        scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)
// Useful constants
#define INF                         INT_MAX
#define EPS                         1e-9
#define INFB						1000000000
// Useful hardware instructions
#define bitcount                    __builtin_popcount
#define gcd                         __gcd
// Useful container manipulation / traversal macros
#define fr(i,a,b)               for(int i=a;i<b;i++)
#define foreach(v, c)               for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define all(a)                      a.begin(), a.end()
#define in(a,b)                     ( (b).find(a) != (b).end())
#define pb                          push_back
#define fill(a,v)                    memset(a, v, sizeof a)
#define sz(a)                       ((int)(a.size()))
#define mp                          make_pair
// Some common useful functions
#define maX(a,b)                     ( (a) > (b) ? (a) : (b))
#define miN(a,b)                     ( (a) < (b) ? (a) : (b))
#define checkbit(n,b)                ( (n >> b) & 1)
#define DREP(a)                      sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind)               (lower_bound(all(arr),ind)-arr.begin())
using namespace std;

// Structures //
typedef pair<int,int> ii;
typedef vector<int> vi;							 
typedef vector<ii> vii;	

int main(){
	int T,N,i=1,j,aux,original,temp;
	set<int> m;
	s(T);
	while(i <= T){
		s(N);
		original = N;
		if(N<=0)printf("case #%d: INSOMNIA\n",i);
		else{
			while(1){
				temp = N;
				while(N > 0){
					aux = N%10;
					N/=10;
					//printf("%d %d \n",aux,N);
					if(m.find(aux) == m.end())m.insert(aux);
				}
				if(m.size() == 10){
					printf("case #%d: %d\n",i,temp);
					break;
				}
				N = original + temp;
			}
		}
		m.clear();
		i++;
	}
	return 0;
}
