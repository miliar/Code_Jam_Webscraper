
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
	scanf("%d", &T);
	for(int p =1; p<=T; p++) {
		int m,n;
		int i,j,k;
		set<int> num;
		scanf("%d",&n);
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				scanf("%d", &k);
				if(i==n-1) {
					num.insert(k);
				}
			}
		}
		int state = 0;
		int val = -1;
		scanf("%d",&m);
		for(i=0;i<4;i++) {
			for(j=0;j<4;j++) {
				scanf("%d",&k);
				if ( i == m-1) {
					if (num.find(k) != num.end()) {
						val = k;
						state ++;
					}
				}
			}
		}
		printf("Case #%d: ", p);
		if (state == 1) {
			printf("%d\n", val);
		} else if (state == 0) {
			printf("Volunteer cheated!\n");
		} else {
			printf("Bad magician!\n");
		}
	}

	return 0;
}
