/**************************************************
 * Author	 : xiaohao Z
 * Blog	 : http://www.cnblogs.com/shu-xiaohao/
 * Last modified : 2015-04-12 00:36
 * Filename	 : A.cpp
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

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T, kase = 1, n;
	char c;
	scanf("%d", &T);
	while(T--) {
		scanf("%d", &n);
		int ans = 0, sum = 0;
		getchar();
		for(int i=0; i<n + 1; i++) {
			scanf("%c", &c);
			int tn = c - '0';
			if(i > sum) {
				ans += (i - sum);
				sum = i;
			}
			sum += tn;
		}
		printf("Case #%d: %d\n", kase ++, ans);
	}
	return 0;
}

