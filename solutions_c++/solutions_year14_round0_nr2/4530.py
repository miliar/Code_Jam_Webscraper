#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>
#include <set>
#include <queue>
#include <string>
#include <map>

using namespace std;
typedef long long ll;
typedef pair<int,int> pr;

int main()
{
	// code here
	int T;
	scanf("%d", &T);
	for (int tc=1; tc<=T; tc++) {
		double ans=0.0;
		double c,f,x;
		double cr=2.0;
		scanf("%lf%lf%lf", &c, &f, &x);
		if (c < x) {
			while (cr * (c*(cr+f) + x*cr) < x * cr * (cr + f)) {
				ans += c/cr;
				cr += f;
			}
			ans += x/cr;
		}
		else {
			ans = x/cr;
		}
		printf("Case #%d: %.7lf\n", tc, ans);
	}

	// code ends here
	return 0;
}
