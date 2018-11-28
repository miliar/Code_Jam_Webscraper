#include <cstdio>
#include <cmath>
#include <cstring>
#include <climits>
#include <cstdlib>
#include <cctype>
#include <iostream>
#include <algorithm>
#include <utility>
#include <string>
#include <vector>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <iterator>

#define MOD 1000000007
#define INF 1000000000000000000
#define PI acos(-1)

using namespace std;

int main()
{
//	freopen("input.in","r",stdin);
//	freopen("output.in","w",stdout);
	int t,y;
	scanf("%d",&t);
	y = 1;
	while (t --) {
		int n,i,j,war,deceit_war,flag,p,q;
		scanf("%d",&n);
		double a[n],b[n];
		int used[n];
		for (i = 0; i < n; i++) {
			scanf("%lf",&a[i]);
		}
		for (i = 0; i < n; i++) {
			scanf("%lf",&b[i]);
		}
		sort(a,a + n);
		sort(b,b + n);
		
		deceit_war = 0;
		p = 0;
		q = n - 1;
		for (i = 0; i < n; i++) {
			if (a[i] > b[p] && b[q] != 1.00) {
				deceit_war++;
				p++;
			} else {
				q--;
			}
		}
		
		war = 0;
		memset(used,0,sizeof(used));
		for (i = 0; i < n; i++) {
			flag = 0;
			for (j = 0; j < n; j++) {
				if (used[j] == 0 && b[j] > a[i]) {
					flag = 1;
					used[j] = 1;
					break;
				}
			}
			if (flag == 0) {
				war++;
			}
		}
		printf("Case #%d: ",y);
		printf("%d %d\n",deceit_war,war);
		y++;
	}
	return 0;
}
