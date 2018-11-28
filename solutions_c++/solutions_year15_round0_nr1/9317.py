#include <climits>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>

#define io_r freopen("input.txt","r",stdin);
#define io_w freopen("output.txt","w",stdout);
#define io_file io_r; io_w;

#define PB push_back
#define MP make_pair
#define f(i,a,b) for (int i = a; i<b; ++i)
#define rep(i,n) for (int i = 0; i<n; ++i)
#define clr(x, y) memset(x, y, sizeof x)
#define all(x) (x).begin(), (x).end()

#define MAX 10010
#define MOD 1000000007

using namespace std;

char s[MAX];
int pd[MAX];

int main (){
	int t, smax;
	scanf("%d", &t);
	
	int k = 0;
	while(t--){
		scanf("%d %s", &smax, s);
		int ans = 0;
		
		pd[0] = 0;
		for(int i = 0; i<=smax; ++i){
			pd[i] += s[i]-'0';
			if(pd[i] <= i) {
				ans++;
				pd[i+1] = pd[i] + 1;
			} else pd[i+1] = pd[i];
		}
		printf("Case #%d: %d\n", ++k, ans);
	}
	return 0;
}
