#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#define int64 long long
#define Sort sort

using namespace std;

map <string, int> words;
int N;
vector <string> line1, line2;
vector <string> line[210];
vector <int> LINE[210];
int cnt[1000000];

vector <string> getAline()
{
	vector <string> ans;
	ans.clear();
	ans.push_back("");
	char ch;
	for (;scanf("%c", &ch) != EOF;)
	{
		if (ch != ' ' && ch != '\n')
			ans[ans.size() - 1] += ch;
		else if (ch == ' ')
				ans.push_back("");
		else break;
	}
	return ans;
}

int main()
{
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);

	int T;
	scanf("%d\n", &T);
	//int res = 999999999;
	for (int ii=0;ii<T;++ii)
	{
		cerr << ii << endl;
		printf("Case #%d: ", ii + 1);
		scanf("%d\n", &N);
		line1 = getAline();
		line2 = getAline();
		for (int i=0;i<N-2;++i)
			line[i] = getAline();
		words.clear();
		int tot = 0;
		for (int i=0;i<N;++i)
			LINE[i].clear();
		for (int i=0;i<line1.size();++i)
		{
			if (words[line1[i]] == 0)
				words[line1[i]] = ++ tot;
			LINE[0].push_back(words[line1[i]]);
		}
		for (int i=0;i<line2.size();++i)
		{
			if (words[line2[i]] == 0)
				words[line2[i]] = ++ tot;
			LINE[1].push_back(words[line2[i]]);
		}
		for (int i=0;i<N-2;++i)
		{
			for (int j=0;j<line[i].size();++j)
			{
				if (words[line[i][j]] == 0)
					words[line[i][j]] = ++ tot;
				LINE[i+2].push_back(words[line[i][j]]);
			}
		}
		// for (int i=0;i<N;++i)
		// {
		// 	for (int j=0;j<LINE[i].size();++j)
		// 		cerr << LINE[i][j] << " ";
		// 	cerr << endl;
		// }
		int res = 99999999;
		for (int tt=0;tt<1 << (N - 2);++tt)
		{
			words.clear();
			for (int i=0;i<=tot;++i) cnt[i] = 0;
			for (int i=0;i<LINE[0].size();++i)
			{
				cnt[LINE[0][i]] |= 1;
			}
			
			int ans = 0;
			for (int i=0;i<LINE[1].size();++i)
				cnt[LINE[1][i]] |= 2;

			for (int i=0;i<N-2;++i)
			{
				for (int j=0;j<LINE[i+2].size();++j)
				{
					if (tt & (1 << i)) cnt[LINE[i+2][j]] |= 2;
					else cnt[LINE[i+2][j]] |= 1;
				}
			}
			for (int i=0;i<=tot;++i) 
				if (cnt[i] == 3) ++ ans;
			res = min(res, ans);
		}
		printf("%d\n", res);
	}

	return 0;
}