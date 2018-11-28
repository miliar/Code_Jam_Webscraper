#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cmath>
#include <ctime>
#include <cctype>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <deque>
#include <bitset>
#include <iostream>
#include <sstream>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair <int, int> pii;
typedef pair <int, pii> piii;
typedef long double ld;

long double eps = 1e-10;
const int N = 200;
int sign(long double x){
	if(x > eps) return 1;
	if(x < -eps)return -1;
	return 0;
}
struct node{
	long double v;
	long double temp;
	node(){};
	node(long double a, long double b){
		v = a;
		temp = b;
	}
}q[N];
bool operator<(node x, node y){
	return x.temp < y.temp;
}

long double min(long double a, long double b){
	if(a < b)return a;
	return b;
}
int main()
{
	int TT;
	scanf("%d", &TT);
	for(int cc = 1; cc <= TT; ++cc){
		int n;
		long double v, temp;
		cin >> n >> v >> temp;
		for(int i=0; i<n; ++i){
			cin >> q[i].v >> q[i].temp; 
		}
		sort(q, q + n);
		if(sign(q[0].temp - temp) == 1 || sign(q[n-1].temp - temp) == -1){
			printf("Case #%d: IMPOSSIBLE\n", cc);
			continue;
		}
		long double low = 0, high = 1e20;
		while(sign(low - high)){
			long double mid = (low + high) / 2;
			long double up = 0, upv = 0, down = 0, downv = 0;
			for(int i=0; i<n; ++i){
				long double now = min(v - downv, q[i].v * mid);
				down *= downv;
				downv += now;
				down = (down + now * q[i].temp) / downv;
			}
			for(int i=n-1; i>=0; --i){
				long double now = min(v - upv, q[i].v * mid);
				up *= upv;
				upv += now;
				up = (up + now * q[i].temp) / upv;
			}
		//	cout<<upv<<"   "<<downv<<"   "<<up<<"   "<<down<<endl;
			if(sign(upv - v) >= 0 && sign(downv - v) >= 0 && sign(up - temp)>=0 && sign(down - temp)<=0){
				high = mid;
			}else{
				low = mid;
			}
		}
		printf("Case #%d: %.10f\n", cc, (double)low);
	}
	return 0;
}

