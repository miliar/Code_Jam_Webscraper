
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
#define debug(a) { for( typeof(a.begin()) it = a.begin() ; it != a.end() ; it++ ) cout << *it << " "; cout << endl; }

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


int main(){
	int T;
	scanf("%d",&T);
	for(int p =1; p<=T; p++) {
		printf ("Case #%d: ", p);
		double c,f,x;
		scanf("%lf%lf%lf", &c,&f,&x);

		int lim = int(x)+1;
		double arr[lim];
		double mintime = x/2;
		int i,j,k;
		for(i=0;i<lim;i++) {
			arr[i] = c/(2+(i)*f);
			if (i !=0) {
				arr[i]+=arr[i-1];
			}
			mintime = min (mintime, arr[i] + x/(2+(i+1)*f));
		}
		printf("%0.7lf\n", mintime);
		
	}

	return 0;
}
