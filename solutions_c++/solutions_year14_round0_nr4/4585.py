/**************************************************
 * Author	 : xiaohao Z
 * Blog	 : http://www.cnblogs.com/shu-xiaohao/
 * Last modified : 2014-04-12 22:23
 * Filename	 : 2014_pre_D.cpp
 * Description	 : 
 * ************************************************/

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <map>
#define MP(a, b) make_pair(a, b)
#define PB(a) push_back(a)

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<unsigned int,unsigned int> puu;
typedef pair<int, double> pid;
typedef pair<ll, int> pli;
typedef pair<int, ll> pil;

const int INF = 0x3f3f3f3f;
const double eps = 1E-6;

bool cmp(double a, double b) {
	return a > b;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T, n;
   	double a[2100], b[2100];
	cin >> T;
	for(int kase = 1; kase <= T; kase++){
		cin >> n;
		for(int i=0; i<n; i++) cin >> a[i];
		for(int i=0; i<n; i++) cin >> b[i];
		sort(a, a+n, cmp);
		sort(b, b+n, cmp);
		int t = 0, i = 0, ta = 0, tb = 0;
		while(t < n){
			while(a[i] > b[t] && t < n){
				i++;t++;ta++;
			}
			while(a[i] <= b[t] && t < n) t++;
		}
		t = 0, i = 0;
		while(t < n){
			while(b[i] > a[t] && t < n){
				i++;t++;tb++;
			}
			while(b[i] <= a[t] && t < n) t++;
		}
		printf("Case #%d: ", kase);
		printf("%d %d\n", ta, n-tb);
	}
	return 0;
}

