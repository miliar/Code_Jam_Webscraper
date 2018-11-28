#include <cstdio>
#include <queue>
#include <vector>

using namespace std;

int T, N;
int P[26];
int S;

struct Cmp
{
	bool operator()(const int& a, const int& b) const
	{
		return P[a] < P[b];
	}
} cmp;

bool check()
{
	for (int i = 0; i < N; i++) {
		if ((P[i] * 2) > S)
			return false;
	}

	return true;
}

int main()
{
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		scanf("%d", &N);

		S = 0;

		priority_queue<int, vector<int>, Cmp> q;
		for (int i = 0; i < N; i++) {
			scanf("%d", &P[i]);
			S += P[i];
			q.emplace(i);
		}


		printf("Case #%d: ", tc);

		while (1) {
			if (q.empty())
				break;

			int one = q.top();
			q.pop();
			P[one]--;
			S--;
			if (P[one] > 0)
				q.push(one);

			printf("%c", one + 'A');
			

			if (q.empty())
				break;

			int two = q.top();
			q.pop();
			P[two]--;
			S--;
			if (P[two] > 0)
				q.push(two);

			if (check()) {
				printf("%c ", two + 'A');
			}
			else {
				printf(" %c", two + 'A');
			}
		}
		printf("\n");
	}

	return 0;
}