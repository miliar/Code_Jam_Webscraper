#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
#include<queue>
#include<algorithm>
#include<map>
#include<iomanip>
#include<set>
using namespace std;

int n;
set<int> S;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	//FILE *out;
	//out = fopen("out.txt", "w+");
	int T, n;
	cin >> T;
	for (int t = 1;t <= T;t++)
	{
		S.clear();
		cin >> n;
		if (n == 0)
		{
			printf("Case #%d: INSOMNIA\n", t);
			//fprintf(out, "Case #%d: INSOMNIA\n", t);
			continue;
		}
		long long tmp;
		for (int i = 1;;i++)
		{
			tmp = n*i;
			while (tmp)
			{
				S.insert(tmp % 10);
				tmp /= 10;
			}
			tmp = n*i;
			if (S.size() == 10)
				break;
		}

		printf("Case #%d: %lld\n", t, tmp);
		//fprintf(out, "Case #%d: %lld\n", t, tmp);
	}
	//fclose(out);
	return 0;
}