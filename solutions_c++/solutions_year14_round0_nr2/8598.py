#include <bits/stdc++.h>

using namespace std;
#define CLR(a) memset(a, 0, sizeof(a))
#define ABS(X) ( (X) > 0 ? (X) : ( -(X) ) )
#define SZ(V) (int )V.size()
#define ALL(V) V.begin(), V.end()
#define RALL(V) V.rbegin(), V.rend()
#define FORN(i, n) for(LL i = 0; i < n; i++)
#define FORAB(i, a, b) for(LL i = a; i <= b; i++)
#define pll pair < long long int, long long int >
#define pii pair < int, int >
#define psi pair < string, int >
#define PB push_back  
#define MP make_pair
#define F first
#define S second
#define MOD 1000000007LL

typedef pair<int,int> PII;
typedef pair<double, double> PDD;
typedef long long LL;

int main(){
	double num_farms,c,f,x,res,rate,prev_tm;
	LL t;
	scanf("%lld",&t);
	FORN(test,t){
		scanf("%lf %lf %lf",&c,&f,&x);
		num_farms=0;
		rate=2.0;
		res=x*(1.0/rate);
		prev_tm=0.0;
		while(num_farms*c<=x){
			// cout << num_farms << " " << c << " " << x << " " << rate << " " << prev_tm + x*(1.0/rate) << endl;
			res=min(res,prev_tm + x*(1.0/rate));
			prev_tm+=c/(1.0*rate);
			num_farms++;
			rate+=f;
		}
		res=min(res,prev_tm + x*(1.0/rate));
		printf("Case #%lld: %lf\n", test+1,res);
	}
	return 0;
}