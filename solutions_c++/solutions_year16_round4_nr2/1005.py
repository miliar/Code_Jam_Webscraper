#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define F first
#define S second
typedef long long LL;


int ntest;
int n,k;
double a[300];

double f(int x){
	vector<double> vt;
	for(int i=0; i<n; i++){
		if( x &(1<<i) )
			vt.pb(a[i]);
			//cout << "a[i] = " << a[i] << endl;
	}
	int t = k/2;
	int s = (1<< t) - 1;
	double res = 0.0;
	while (!(s & 1 << k)){
		double temp = 1.0;
    	for(int i=0; i<vt.size(); i++){
    		if ( s & (1<<i)) temp *= vt[i];
    		else temp *= (1-vt[i]);
		}
		res += temp;
    	int lo = s & ~(s - 1);       // lowest one bit
    	int lz = (s + lo) & ~s;      // lowest zero bit above lo
    	s |= lz;                     // add lz to the set
    	s &= ~(lz - 1);              // reset bits below lz
    	s |= (lz / lo / 2) - 1;      // put back right number of bits at end
	}
	return res;
}
void solve(int test){
	printf("Case #%d: ",test+1);
	scanf("%d %d",&n,&k);
	for(int i=0; i<n;i++) scanf("%lf",&a[i]);
	double res = 0.0;
	int s = (1<< k) - 1;
	while (!(s & 1 << n)){
    	res = max(res, f(s) );
    	int lo = s & ~(s - 1);       // lowest one bit
    	int lz = (s + lo) & ~s;      // lowest zero bit above lo
    	s |= lz;                     // add lz to the set
    	s &= ~(lz - 1);              // reset bits below lz
    	s |= (lz / lo / 2) - 1;      // put back right number of bits at end
	}
	printf("%.6lf\n",res);
}

int main(){
	freopen("B-small-attempt0.in","r",stdin);
  	freopen("test.out","w",stdout);
  	scanf("%d",&ntest);
  	for(int test=0; test<ntest; test++){
  		solve(test);
	}
  	return 0;
}


