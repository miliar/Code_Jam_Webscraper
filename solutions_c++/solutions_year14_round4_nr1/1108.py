#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>

using namespace std;

int N, X;
int S[10005], Used[10005];

void Work()
{
	scanf("%d%d", &N, &X);
	for (int i = 0; i < N; i ++)
		scanf("%d", &S[i]);
	sort(S, S + N);
	multiset <int> Set;
	for (int i = 0; i < N; i ++)
		Set.insert(-S[i]);

	int Ans = 0;
	while (! Set.empty())
	{
		Ans ++;
		int Cur = - *Set.begin();
		Set.erase(Set.begin());
		int Remain = X - Cur;
		multiset <int> :: iterator it = Set.lower_bound(-Remain);
		if (it != Set.end())
			Set.erase(it);
	}
	printf("%d\n", Ans);
	fflush(stdout);
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
    int Cases;
    scanf("%d", &Cases);
    for (int Case = 1; Case <= Cases; Case ++)
    {
		printf("Case #%d: ", Case);
		Work();
    }
    return 0;
}