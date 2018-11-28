#include<cstdlib>
#include<cctype>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<iostream>
#include<sstream>
#include<fstream>
#include<bitset>
#include<list>
using namespace std;
const double EPS = 0.00000001;

int main()
{
	freopen("E:\\D.in", "r", stdin);
	freopen("E:\\D.out", "w", stdout);
	vector<float> Naomi;
	vector<float> Ken;
	int T;
	cin >> T;
	for (int cas = 0; cas < T; cas++)
	{
		Naomi.clear();
		Ken.clear();
		int x = 0;
		int y = 0;

		int N;
		cin >> N;
		for (int i = 0; i < N; ++i)
		{
			float temp = 0;
			cin >> temp;
			Naomi.push_back(temp);
		}
		sort(Naomi.begin(), Naomi.end());
		for (int i = 0; i < N; ++i)
		{
			float temp = 0;
			cin >> temp;
			Ken.push_back(temp);
		}
		sort(Ken.begin(), Ken.end());

		int p1 = N - 1;
		int p2 = N - 1;
		while (p1 >= 0 && p2 >= 0)
		{
			float naomi = Naomi.at(p1);
			float ken = Ken.at(p2);
			if (naomi - ken > EPS)
			{
				x++;
				p1--;
				p2--;
			}
			else
			{
				p2--;
			}
		}

		int p3 = N - 1;
		int p4 = N - 1;
		while (p3 >= 0 && p4 >= 0)
		{
			float naomi = Naomi.at(p3);
			float ken = Ken.at(p4);
			if (ken - naomi > EPS)
			{
				p3--;
				p4--;
			}
			else
			{
				y++;
				p3--;
			}
		}

		printf("Case #%d: %d %d\n", cas + 1, x, y);
	}

	return 0;
}
