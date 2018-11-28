#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <sstream>
#include <functional>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <list>
#include <numeric>
using namespace std;
const double PI = 3.14159265358979323846;
const double EPS = 1e-12;
const int INF = 1<<25;
typedef pair<int,int> P;
typedef long long ll;
typedef unsigned long long ull;


int main(){
	int T;
	cin>>T;
	for(int Case = 1; Case <= T; Case++){
		int h, w, q;
		cin>>h>>w>>q;
		vector<vector<int> > g(h, vector<int>(w, 0));
		int res = INF;
		int m = h*w;
		for(int i = 0; i < 1<<m; i++){
			if(__builtin_popcount(i)==q){
				for(int j = 0; j < h; j++){
					for(int k = 0; k < w; k++){
						g[j][k] = 1&(i>>(j*w+k));
					}
				}
				int r = 0;
				for(int j = 0; j < h; j++){
					for(int k = 0; k < w; k++){
						if(!g[j][k]) continue;
						if(j+1<h && g[j+1][k]) r++;
						if(k+1<w && g[j][k+1]) r++;
					}
				}
				res = min(res, r);
			}
		}
		printf("Case #%d: %d\n", Case, res);
	}
	return 0;
}

