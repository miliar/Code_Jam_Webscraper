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
bool myfunc(double l, double r){
	return r < l;
}
int main()
{
	int t, i, j, n, k, m, h = 0;
	cin>>t;
	while(++h <= t){
		cin>>n;
		int count = 0;
		double a[1010] = {0}, b[1010] = {0};
		for(i = 0; i < n; ++i) cin>>b[i];     //NAOMI
		for(i = 0; i < n; ++i) cin>>a[i];    //KEN
		sort(a, a+n, myfunc);
		sort(b, b+n, myfunc);
		/*for(i = 0; i < n; ++i) cout<<a[i]<<" ";
		cout<<endl;
		for(i = 0; i < n; ++i) cout<<b[i]<<" ";
		cout<<endl;
		*/
		k = n;
		for(i = 0; i < k; ){
			for(j = 0; j < n; ++j){
				if(b[i] < a[j]) --k;
				else ++i, ++count;
			}
		}
		cout<<"Case #"<<h<<": "<<count<<" ";
		count = 0;
		k = n;
		for(i = 0; i < k; ){
			for(j = 0; j < n; ++j){
				if(a[i] < b[j]) --k, ++count;
				else ++i;
			}
		}
		cout<<count<<endl;
	}
	return 0;
}

