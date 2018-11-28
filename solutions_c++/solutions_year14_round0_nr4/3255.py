
/*Paresh Verma*/
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
#include <cstring>
#include <queue>		//max heap implementation
#include <limits.h>

#define pub push_back
#define pob pop_back
#define puf push_front
#define pof pop_front
#define mkp make_pair
#define fi first
#define se second
#define LL long long
#define fill(x,y) memset(x, y, sizeof(x))
#define debug(a) { for( typeof(a.begin()) it = a.begin() ; it != a.rbegin() ; it++ ) cout << *it << " "; cout << rbeginl; }

using namespace std;

//class comparators for queue and others
class classcomp{
	public:
		bool operator() (const int& l, const int& r)const{
			return l<r;
		}
};

int dx[]={1,0,-1,0};
int dy[]={0,1,0,-1};

bool cmplt(double a, double b) {
	if (fabs(a-b) < 0.000001)
		return false;
	return a<b;
}

int main(){
	int T;
	scanf("%d",&T);
	for(int p = 1; p <= T; p++) {
		printf("Case #%d: ", p);
		int n;
		scanf("%d", &n);
		int i,j,k;
		double x,y;
		set<double> a1, a2;
		for(i=0;i<n;i++) {
			scanf("%lf",&x);
			a1.insert(x);
		}
		for(i=0;i<n;i++) {
			scanf("%lf",&x);
			a2.insert(x);
		}
		set<double>::iterator it;
		/*
		for(it=a1.begin(); it!= a1.end();it++)
			printf("%lf ", *it);
		printf("\n");
		for(it=a2.begin(); it!= a2.end();it++)
			printf("%lf ", *it);
		printf("\n");
		*/
		//a1 Naomi, a2 ken
		int pts1=0, pts2=0;

		set<double> b1 = a1, b2 = a2;
		while(b2.size() > 0) {
			if (cmplt(*(b1.begin()), *(b2.begin()))) {
				pts2++;
				b1.erase(b1.begin());
				b2.erase(b2.begin());
			} else {
				b2.erase(b2.begin());
			}
		}
		pts2= n -pts2;

		while(a1.size() > 0 && a2.size() > 0){
			it = a1.upper_bound(*(a2.begin()));
			if (it == a1.end()) {
				break;
			} else {
				a1.erase(it);
				a2.erase(a2.begin());
				pts1++;
			}
		}

		printf("%d %d\n", pts1, pts2);
	}

	return 0;
}
