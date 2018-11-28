#include <algorithm>
#include <functional>
#include <vector>
#include <map>    
#include <cstdio>
#include <queue>
#include <climits>
#include <stack>
#include <set>
#include <cmath>
#include <cstring>
#include <list>
using namespace std;

typedef long long ll;

const int INF = 987654321;
const ll INFF = 987654321213;
const ll MOD = 987654321;
const ll PLUS = 1000000;

int t, n;
bool visited[11];
int main() {
#ifdef _CONSOLE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);
#endif

	scanf("%d", &t);

	for (int testCase = 1; testCase <= t; testCase++) {

		memset(visited, 0, sizeof(visited));
		scanf("%d", &n);
		
		int cnt = 0;
		for ( int i=1; ; i++ ) {
			cnt++;
			int temp = n;

			while (temp) {
				visited[temp % 10] = true;
				temp /= 10;
			}
			bool flag = true;
			for (int i = 0; i <= 9; i++) {
				if (visited[i] == false) {
					flag = false; break;
				}
			}
			if (flag == true) {
				printf("Case #%d: %d\n", testCase, n); break;
			}
			if (cnt == 1000) {
				printf("Case #%d: INSOMNIA\n", testCase); break;
			}
			n = (n / i)*(i + 1);
		}		
	}

}
