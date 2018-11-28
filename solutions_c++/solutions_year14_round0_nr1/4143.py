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
	int t, i, j, n, m, k, h = 0;
	cin>>t;
	while(++h <= t){
		int a[4][4] = {{0}}, b[4][4] = {{0}};
		cin>>n;
		int count = 0, p = -1;
		for(i = 0; i < 4; ++i)
			for(j = 0; j < 4; ++j) cin>>a[i][j];
		cin>>m;
		for(i = 0; i < 4; ++i){
			for(j = 0; j < 4; ++j){
				 cin>>b[i][j];
				 if(i == m-1){
				 	for(k = 0; k < 4; ++k) if(b[i][j] == a[n-1][k]) p = k, ++count;//, cout<<"@ = "<<a[n][k]<<endl;
				 }
			}
		}
		if(count == 1) cout<<"Case #"<<h<<": "<<a[n-1][p]<<endl;
		else if(count > 1) cout<<"Case #"<<h<<": Bad magician!\n";
		else cout<<"Case #"<<h<<": Volunteer cheated!\n";
	}
	return 0;
}
