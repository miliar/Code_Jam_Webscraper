#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <utility>

using namespace std;

const long long Modulo = 1000002013;

int N, M;

long long Cost(int d)
{
	if (d == 0)
		return 0;
	return ((long long) (N + N - d + 1) * (long long) d / 2) % Modulo;
}

pair <long long, long long> Pair[3000];
long long Stack[10000][2], nStack;

void Work(int Case)
{
	scanf("%d%d", &N, &M);
	long long OrigCost = 0;
	for (int i = 0; i < M; i ++)
	{
		int A, B, C;
		scanf("%d%d%d", &A, &B, &C);
		OrigCost = (OrigCost + (Cost(B - A) * C) % Modulo) % Modulo;
		Pair[i * 2] = make_pair(A, -C);
		Pair[i * 2 + 1] = make_pair(B, C);
	}
	sort(Pair, Pair + (2 * M));
	long long CurCost = 0;
	for (int i = 0; i < M * 2; i ++)
	{
		if (Pair[i].second == 0)
			continue;
		if (Pair[i].second < 0)
		{
			if (nStack == 0 || Stack[nStack - 1][0] != Pair[i].first)
			{
				nStack ++;
				Stack[nStack - 1][0] = Pair[i].first;
				Stack[nStack - 1][1] = -Pair[i].second;
			}
			else
				Stack[nStack - 1][1] += -Pair[i].second;
		}
		else
		{
			long long Remain = Pair[i].second;
			while (Remain)
			{
				long long Use = min(Stack[nStack - 1][1], Remain);
				CurCost = (CurCost + Cost(Pair[i].first - Stack[nStack - 1][0]) * Use) % Modulo;
				Stack[nStack - 1][1] -= Use;
				Remain -= Use;
				if (Stack[nStack - 1][1] == 0)
					nStack --;
			}
		}
	}

	printf("Case #%d: %d\n", Case, (OrigCost - CurCost + Modulo) % Modulo);
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int Cases;
	scanf("%d", &Cases);
	for (int i = 1; i <= Cases; i ++)
		Work(i);
	return 0;
}