/* Magic Trick */
/* produced by wegnahz */
#include <iostream>
#include <string>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
using namespace std;
#define skip(x) for(int i=1;i<=(x);++i) getchar();
#define xx first
#define yy second
#define MP make_pair
#define two(X) (1<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define fill0(a) memset(a,0,sizeof(a));
typedef pair<int,int> ipair;
const int inf=0x3FFFFFFF;
const double pi=acos(-1.0);
const double eps=1e-8;
const int move[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}
inline void fill(int *a,int b,int c){
  for (int i=0;i<c/4;i++,a++) *a=b;}
inline void show(int *a,int n){
  for (int i=0;i<=n;i++) cout<<a[i]<<' ';cout<<endl;}
int num,n,m;
int main(){
    int tt,ii;
    #ifndef ONLINE_JUDGE
    freopen("Magic Trick.in","r",stdin);
    freopen("Magic Trick.out","w",stdout);
    #endif
    
    cin >> tt;
    for (int ii = 1; ii <= tt; ++ii) {
    	int ans1, ans2;
    	int square1[4][4], square2[4][4];
    	cin >> ans1; --ans1;
    	for (int i = 0; i < 4; ++i) for (int j = 0; j < 4; ++j)
    		cin >> square1[i][j];
    	cin >> ans2; --ans2;
    	for (int i = 0; i < 4; ++i) for (int j = 0; j < 4; ++j)
    		cin >> square2[i][j];
    	set<int> mset;
    	for (int j = 0; j < 4; ++j) mset.insert(square1[ans1][j]);
    	vector<int> ans;
		for (int j = 0; j < 4; ++j)
			if (mset.find(square2[ans2][j]) != mset.end())
				ans.push_back(square2[ans2][j]);
		cout << "Case #" << ii << ": ";
		if (ans.size() == 1)
			cout << ans[0] << endl;
		else if (ans.size() == 0)
			cout << "Volunteer cheated!" << endl;
		else
			cout << "Bad magician!" << endl;
	}
    return 0;
}
