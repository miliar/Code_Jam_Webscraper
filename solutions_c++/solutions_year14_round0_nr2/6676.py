#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define all(Con) Con.begin(),Con.end()

using namespace std;
int tests;
double C,F,X;
int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	//scanf("%d\n",&tests);
	cin>>tests;
	for(int counter=1;counter<=tests;counter++){
		scanf("%lf %lf %lf\n",&C,&F,&X);
		// cin>>C>>F>>X;
		// C = 10000.0;
		// F = 2.0;
		// X = 100000.0;

		double ans = 0.0;
		int n = 0;
		while(true){
			// if(n>1000){ cout<<"Too big N\n"; break; }
			double xN = X/(2.0+n*F);
			double xN1 = X/(2.0+(n+1)*F);
			double cN = C/(2.0+n*F);

			if(xN > xN1+cN){
				ans+=cN;
				n++;
			} else {
				ans+=xN;
				break;
			}
			// cerr<<xN<<" "<<" "<<xN1<<" "<<cN<<"ans :"<<ans<<"\n"; 
		}

		printf("Case #%d: %.7lf\n",counter,ans);
	}

return 0;
}
