#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
const int N = 100010;
const LL MOD = 1000000007;

int main(){

	freopen("A-small-attempt0.in", "r", stdin); /*如果in.txt不在连接后的exe的目录，需要指定路径如D:\\in.txt*/
	freopen("out.txt", "w", stdout);/*同上*/
	int T, x, y,tmp;
	cin >> T;
	for (int t = 1; t <= T; t++){
		cin >> x;
		vector<int>s,e;
		for (int i = 1; i <= 4; i++){
			for (int j = 1; j <= 4; j++){
				cin >> tmp;
				if (x == i) s.push_back(tmp);
			}
		}

		cin >> y;
		for (int i = 1; i <= 4; i++){
			for (int j = 1; j <= 4; j++){
				cin >> tmp;
				if (i == y) e.push_back(tmp);
			}
		}
		int cnt = 0;
		int ans = -1;
		for (int i = 1; i <= 4; i++){
			for (int j = 1; j <= 4; j++){
				if (s[i - 1] == e[j - 1]) {
					cnt++;
					ans = s[i - 1];
				}
			}
		}
		printf("Case #%d: ",t);


		if (cnt == 0) puts("Volunteer cheated!");
		else if (cnt == 1) cout << ans << endl; 
		else puts(" Bad magician!");
	}
}