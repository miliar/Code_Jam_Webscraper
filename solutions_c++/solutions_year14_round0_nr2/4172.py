#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
const double pi=acos(-1.0);
const double eps=1e-11;
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}
typedef pair<int,int> ipair;
#define SIZE(A) ((int)A.size())
#define LENGTH(A) ((int)A.length())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)
#define S(x) scanf("%d",&x)
int main()
{
	int t, i, j;
	double c, f, x, mini = 0;
	int h = 0;
	cin>>t;
	while(++h <= t){
		cin>>c>>f>>x;
		//if(c < x){
			double tot_time = 0;
			mini = 9999999999.0;
			tot_time += c/2.0;
			double t1 = 0, t2 = 0;
			i = 1;
			mini =  x/(2.0+i*f);
			while(1) {
				t1 +=  c/(2.0+i*f) + x/(2.0+(i+1)*f);
				if(mini < t1) break;
				else {
					mini = t1;
					t1 -= x/(2.0+(i+1)*f);
				}
				++i;
			}		
			printf("Case #%d: %.6f\n", h, min((mini+tot_time),x/2.0));
		/*} else {
			//cout<<x/2<<endl;
			printf("%Case #%d: %.6f\n", h, x/2.0);
		}*/
		
	}
	return 0;
}

