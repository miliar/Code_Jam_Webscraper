#include <bits/stdc++.h>
using namespace std;

#define rep(i,a,b) for(int i(a); i < (b); i++)

#define all(c) c.begin(), c.end()
#define UNIQUE(c) { sort(all(c)); (c).resize( unique(all(c))-c.begin() ); }
#define pb push_back

#define D(x) if(1) cout << __LINE__ <<" "<< #x " = " << (x) << endl;
#define D2(x,y) cout << #x " = " << x << "  " << #y " = " << y << endl;
#define DVEC(v,n) {cout<<#v<<"[] ={ "; rep(i,0,n) cout<<v[i]<<" "; cout << "}\n";}

#define mp make_pair
#define fst first
#define snd second

#define isONE(mask,bit) ((mask & (1<<bit))>0
#define isZERO(mask,bit) ((mask & (1<<bit))==0
#define setBIT(mask,bit) (mask | (1<<bit))
#define clearBIT(mask,bit) (mask & ~(1<<bit))
#define toogleBIT(mask,bit) (mask ^ (1<<bit))
#define LSOne(mask) (mask &(-mask))

typedef pair<int,int> ii;
typedef long long ll;


int main(){

	// freopen("A-large.in", "r", stdin);
	// freopen("A-large-output.txt", "w", stdout);

	int t, passo, caso = 1;
	ll N;
	scanf("%d", &t);
	while (t--) {
		
		scanf("%lld", &N);
		passo = N;
		int v[10]; memset(v, 0, sizeof v);
		
		if (N == 0) printf("Case #%d: INSOMNIA\n", caso++);
		else{
			while(1){
				ll NN = N;
				while (NN){
					v[NN%10] = 1;
					NN /= 10;
				}
				
				int fill = 0;
				rep(i,0,10) fill += v[i];
				if(fill == 10) {
					 printf("Case #%d: %lld\n", caso++, N);
					break;
				}
				N += passo;
			}
		}
	}
	return 0;
}

