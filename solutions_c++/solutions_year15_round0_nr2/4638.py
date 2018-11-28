#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;

vvpii n;
int d;

int calc (vector<int> o, int i) {
	if (i == d) {
		int temp = 0;
		int s = 0;
		for (int j = 0; j < o.size(); ++j)
		{
			pii a = n[j][o[j]];
			temp = max(temp, a.first);
			s += a.second;
		}
		return temp + s;
	}
	else {
		int ret = 1 << 30;
		for (int j = 0; j < n[i].size(); ++j)
		{
			vector<int> newo;
			newo = o;
			newo.push_back(j);
			ret = min(ret, calc(newo, i+1));
		}
		return ret;
	}
}


int main(int argc, char const *argv[])
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t)
	{
		scanf("%d", &d);
		n = vvpii(d);
		for (int i = 0; i < d; ++i)
		{
			int x;
			scanf("%d", &x);
			n[i].push_back(pii(x, 0));
			for (int divs = 2; divs <= x; ++divs)
			{
				int temp;
				if (x % divs == 0)	temp = x / divs;
				else				temp = x / divs + 1;
				if (temp+divs-1 < x) {
					n[i].push_back(pii(temp, divs-1));
				}
			}
		}

		int resp = calc(vector<int>(), 0);



		printf("Case #%d: %d\n", t, resp);
	}

	return 0;
}