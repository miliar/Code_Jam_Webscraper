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
	freopen("input.in","r",stdin);
	freopen("output.in","w",stdout);
	int t,y;
	scanf("%d",&t);
	y = 1;
	while (t --) {
		vector <int> v;
		int n,m,i,j;
		int a[5][5],b[5][5];
		scanf("%d",&n);
		for (i = 1; i <= 4; i++) {
			for (j = 1; j <= 4; j++) {
				scanf("%d",&a[i][j]);
			}
		}
		scanf("%d",&m);
		for (i = 1; i <= 4; i++) {
			for (j = 1; j <= 4; j++) {
				scanf("%d",&b[i][j]);
			}
		}
		for (i = 1; i <= 4; i++) {
			for (j = 1; j <= 4; j++) {
				if (a[n][i] == b[m][j]) {
					v.push_back(a[n][i]);
				}
			}
		}
		printf("Case #%d: ",y);
		if (v.size() == 0) {
			printf("Volunteer cheated!\n");
		} else if (v.size() > 1) {
			printf("Bad magician!\n");
		} else {
			printf("%d\n",v[0]);
		}
		y++;
	}
	return 0;
}
