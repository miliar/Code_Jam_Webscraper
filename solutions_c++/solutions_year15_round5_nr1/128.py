#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;
typedef pair < int, int > pii;

const int MAX = 1000020;

int n, D, salary[MAX], manager[MAX];
vector < int > children[MAX];

bool alive[MAX];

void initAlive() {
	int i;
	for(i = 0; i < n; i++)
		alive[i] = 1;
}

int kill(int target) {
	if(alive[target] == 0) return 0;
	alive[target] = 0;

	int ret = 1;

	int i;
	for(i = 0; i < children[target].size(); i++) {
		ret += kill(children[target][i]);
	}

	return ret;
}

int heal(int target, int up, int down) {
	if(alive[target] == 1 || alive[manager[target]] == 0) return 0;
	alive[target] = 1;

	int ret = 1;

	int i;
	for(i = 0; i < children[target].size(); i++) {
		int index = children[target][i];
		if(down <= salary[index] && salary[index] <= up) {
			ret += heal(index, up, down);
		}
	}

	return ret;
}

int main() {
	freopen("A.out", "w", stdout);

	int numCase, nowCase;
	scanf("%d", &numCase);

	for(nowCase = 1; nowCase <= numCase; nowCase++) {
		scanf("%d%d", &n, &D);

		vector < pii > sorted;

		int i;
		{
			int s, A_s, C_s, R_s;
			int m, A_m, C_m, R_m;

			scanf("%d%d%d%d", &s, &A_s, &C_s, &R_s);
			scanf("%d%d%d%d", &m, &A_m, &C_m, &R_m);

			salary[0] = s;
			manager[0] = 0;
			sorted.push_back(pii(salary[0], 0));
			for(i = 1; i < n; i++) {
				s = (s*A_s + C_s)%R_s;
				m = (m*A_m + C_m)%R_m;

				salary[i] = s;
				manager[i] = m%i;
				children[m%i].push_back(i);

				sorted.push_back(pii(salary[i], i));
			}
		}

		sort(sorted.begin(), sorted.end());

		int res = 0;
		{
			initAlive();

			int nowAlive = n, s = 0, e = n;
			//CEO보다 월급 큰 놈들 죽이고 시작
			while(salary[sorted[e-1].second] > salary[0]) {
				nowAlive -= kill(sorted[e-1].second);
				e--;
			}

			//월급 작은 놈들은 CEO가 최대 월급이 될 수 있도록 죽임
			while(salary[sorted[s].second] < salary[0]-D) {
				nowAlive -= kill(sorted[s].second);
				s++;
			}

			//죽이고 난 이후 살릴 놈은 다시 살린다
			while(e < n && salary[sorted[e].second]-salary[sorted[s].second] <= D) {
				nowAlive += heal(sorted[e].second, salary[sorted[e].second], salary[sorted[s].second]);
				e++;
			}

			res = max(res, nowAlive);

			for(; salary[sorted[s].second] < salary[0];) {
				//타겟이랑 월급 같은 놈들은 다 죽인다
				do {
					nowAlive -= kill(sorted[s].second);
					s++;
				} while(salary[sorted[s].second] == salary[sorted[s-1].second]);

				//죽이고 난 이후 살릴 놈은 다시 살린다
				while(e < n && salary[sorted[e].second]-salary[sorted[s].second] <= D) {
					nowAlive += heal(sorted[e].second, salary[sorted[e].second], salary[sorted[s].second]);
					e++;
				}

				res = max(res, nowAlive);
			}
		}

		printf("Case #%d: %d\n", nowCase, res);

		for(i = 0; i < n; i++)
			children[i].clear();
	}

	return 0;
}