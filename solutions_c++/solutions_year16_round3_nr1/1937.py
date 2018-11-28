#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <random>

using namespace std;

const char* name = "A-large";

char input[100];
char output[100];
char ans[10000];
int p[30];

void generateFileNames()
{
	sprintf(input, "%s.in", name);
	sprintf(output, "%s.out", name);
	freopen(input, "r", stdin);
	freopen(output, "w", stdout);
}

int main()
{
	generateFileNames();
	int T;
	scanf("%d", &T);
	for (int test = 1; test <= T; test++)
	{
		int n;
		scanf("%d", &n);
		set<pair<int, int>> s;
		int sum = 0;
		for (int i = 0; i < n; i++)
		{
			scanf("%d", &p[i]);
			sum += p[i];
			s.insert(make_pair(p[i], i));
		}
		int pos = 0;
		while (!s.empty())
		{
			auto v1 = *s.rbegin();
			auto n1 = v1;
			auto v2 = v1;
			auto n2 = v2;
			s.erase(v1);
			if (v1.first > 1)
			{
				n1.first--;
				s.insert(n1);
			}
			if (!s.empty())
			{
				v2 = *s.rbegin();
				s.erase(v2);
				if (v2.first > 1)
				{
					n2 = v2;
					n2.first--;
					s.insert(n2);
				}
				if (s.empty())
				{
					ans[pos++] = 'A' + v1.second;
					ans[pos++] = 'A' + v2.second;
				}
				else
				{
					if ((sum - 2) < 2 * s.rbegin()->first)
					{
						s.insert(v2);
						s.erase(n2);
						ans[pos++] = 'A' + v1.second;
						sum--;
					}
					else
					{
						ans[pos++] = 'A' + v1.second;
						ans[pos++] = 'A' + v2.second;
						sum -= 2;
					}
				}
			}
			else
			{
				ans[pos++] = 'A' + v1.second;
			}
			ans[pos++] = ' ';
		}
		ans[pos] = 0;
		printf("Case #%d: %s\n", test, ans);
	}
	return 0;
}