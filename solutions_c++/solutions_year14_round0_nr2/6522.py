#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
using namespace std;
#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)

typedef long long ll;
#define INF (1<<29)

int main(){
	int tc, t;
	cin >> t;
	REP(tc,t){
		double c, f, x, num, prd;
		cin >> c >> f >> x;
		bool flag=false;
		prd=2.;
		num=0.;
		while(!flag){
			if(x/prd<c/prd+x/(prd+f)){
				flag=true;
				num+=x/prd;
			}
			else{
				num+=c/prd;
				prd+=f;
			}
		}
		cout << "Case #" << tc+1 << ": ";
		printf("%.7lf",num);
		puts("");
	}
	return 0;
}

