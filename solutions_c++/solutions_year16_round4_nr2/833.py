#include <stdio.h>
#include <vector>
#include <string.h>
#include <algorithm>
using namespace std;

double prob[20];
vector<double> probs;

double dd[20][20];
bool bb[20][20];

double D(int a, int b)
{
	if (a == 0 && b == 0) return 1.0;
	if (bb[a][b] == false)
	{
		if (b == 0) dd[a][b] = D(a - 1, b) * (1 - probs[a-1]);
		else if (a == b) dd[a][b] = D(a - 1, b - 1) * probs[a-1];
		else
		{
			dd[a][b] = probs[a-1] * D(a - 1, b - 1) + (1 - probs[a-1]) * D(a - 1, b);
		}
		bb[a][b] = true;
	}
	return dd[a][b];
}

double getprob(const vector<char> &choose)
{
	probs.clear();
	memset(dd, 0, sizeof(dd));
	memset(bb, 0, sizeof(bb));
	probs.clear();
	for (int i = 0; i < choose.size(); i++)
	{
		if (choose[i]) probs.push_back(prob[i]);
	}

	return D(probs.size(), probs.size() / 2);
}

int main()
{
	freopen(R"(C:\Users\Unused\Downloads\B-small-attempt1.in)", "r", stdin);
	freopen(R"(C:\Users\Unused\Downloads\B-small.out)", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; tt++)
	{
		fprintf(stderr, "%d:%d\n", tt, T);
		printf("Case #%d: ", tt);

		int n, k;
		scanf("%d%d", &n, &k);

		for (int i = 0; i < n; i++)
		{
			scanf("%lf", &prob[i]);
		}

		vector<char> choose;
		for (int i = 0; i < k; i++) choose.push_back(1);
		for (int i = k; i < n; i++) choose.push_back(0);
		sort(choose.begin(), choose.end());

		double ans = 0;
		do
		{
			ans = max(ans, getprob(choose));
		} while (next_permutation(choose.begin(), choose.end()));

		printf("%.9f\n", ans);
	}
}