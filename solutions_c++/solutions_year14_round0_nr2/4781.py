#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector> 
#include<cstring>
#include<string>
#define mp make_pair
#define scn second
#define frs first
#define pb push_back
#define NAME "a"
#define fop freopen(NAME ".in", "r", stdin); freopen(NAME ".txt", "w", stdout); 
using namespace std;

typedef unsigned long long ull;
typedef long long ll;    	
typedef pair<int, int> pi;

void dout() { cerr << endl; }
template <typename Head, typename... Tail>
void dout(Head H, Tail... T) {
  cerr << H << ' ';
  dout(T...);
}
const double eps = 1e-8;
double c, f, x;                                    
int main(){
	#ifdef LocalHost
		fop;
	#endif
	int t;
	scanf("%d", &t);
	int y = 1;

	while (t --> 0) {
		double d = 0, add = 2.0;
		scanf("%lf%lf%lf", &c, &f, &x);
	    while (1) {
	    	double d1 = x/add;
	    	double d2 = c/add + x / (add + f);
	    	if (d1 - d2 > -eps) {
	    		d += c/add;
	    		add += f;
	    		continue;
	    	}
	    	else {
	    		d += d1;	
	    		break;	    			
	    	}
	   	} 	
	   	printf("Case #%d: %lf\n", y++, d);
	}
		
	return 0;
}