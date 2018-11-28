#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <queue>
#include <utility>
#include <vector>
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
#define MSG(a) cout << #a << " = " << a << endl;

int main(){
		
		int t;
		scanf("%d",&t);
		int tcase = 1;
		while(t--){
			
				double C, F, X;
				scanf("%lf %lf %lf",&C, &F, &X);
				double cVel = 2;
				double nVel;
				double ans = 0.0;
				while(1){
					nVel = cVel + F;
					if(C*nVel + X*cVel >= X*nVel){
							//cout<<ans<<endl;
							printf("Case #%d: %.7lf\n",tcase++,(ans + X / cVel));
							break;
					}
					else{
							ans += C / cVel;
							cVel += F;							
					}
					
				}
				
		}


return 0;
}
