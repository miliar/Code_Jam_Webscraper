#include <cstdio>
#include <deque>
#include <set>
#include <string>
#include <map>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <queue>
using namespace std;
typedef long long LL;

#define Debug(x) (cerr << #x << " = " << (x) << endl)
#define Debug2(x, y) (cerr << #x << " = " << (x) << ", " << #y << " = " << (y) << endl)
template<class T> inline T& RD(T &x){  
    char c; for (c = getchar(); c < '0'; c = getchar()); x = c - '0'; for (c = getchar(); '0' <= c && c <= '9'; c = getchar()) x = x * 10 + c - '0';  
    return x;  
}

const int maxn = 100005;

int main(){
	int T;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin >> T;
	int cas = 1;
	double c,f,x;
	while(T --){
		cin >> c >> f >> x;
		double ans = 1e10,tmp,ff;
		ff = 2.0;
		tmp = 0;
		while(1){
			double remain = x/ff + tmp;
			if(remain < ans){
				ans = remain;
			}
			else break;
			tmp += c/ff;
			ff += f;
		}
		printf("Case #%d: %lf\n", cas++,ans);		
	}
}

