#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <map>
#include <set>
#include <vector>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

#define f first
#define s second
#define next qwertyusdfgh
#define read(x) scanf("%d", &x)
#define write(x) printf("%d ", x)
#define writeln(x) printf("%d\n", x)
#define pb push_back
#define mp make_pair

//-------------------------------------------------------------------------------------------------

int main() {

	int tt;
	cin >> tt;
	for (int t = 0; t < tt; t++) {
		double c, f, x;
		cin >> c >> f >> x;
		

		double cur = 0;
		double ans = x / 2;
		double inc = 2;
		while (1) {
			cur += c / inc;
			inc += f;
			if (cur > ans)
				break;
			ans = min(ans, cur + x / inc);
		}
		printf("Case #%d: %.10f\n", t + 1, ans);
	}
	
	return 0;
}