#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <utility>
#include <cmath>
#include <string>
#include <vector>
#include <set>
#include <map>
#define MAXN 105
#define MAXLEN 12005
#define MAXW 2205

using namespace std;

const int INF = 1000*1000*1000;

static set<int> datas[MAXN];

int main ()
{
	int T, iT;
	scanf("%d",&T);
	static char data[MAXLEN];
	//static set<int> ans;
	//static set<int> dist[MAXN][MAXN];
	static map<string, int> wordMap;
	static char ww[MAXW][2];
	for (iT = 0; iT < T; iT++)
	{
		int n;
		scanf("%d\n",&n);
		
		//vector < vector<int> > c (n, vector<int> (n));
		//int s, t;
		//s = 0; t = 1;

		wordMap.clear();
		int wordCount = 0;
		for (int i = 0; i < n; i++)
		{
			fgets(data, MAXLEN, stdin);
			datas[i].clear();
			int len = strlen(data);
			//while (data[len-1] <= 32) len--;
			int j = 0;


			while (j < len)
			{
				string str = "";
				while ((j < len) && (data[j] != ' '))
				{
					str += data[j];
					j++;
				}
				j++;
				int wordNo;
				map<string,int>::iterator it;
				it = wordMap.find(str);
				if (it == wordMap.end())
				{
					wordNo = wordCount;
					wordCount++;
					wordMap[str] = wordNo;
				}
				else
				{
					wordNo = it->second;
				}
				datas[i].insert(wordNo);
			}
		}

/*
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				dist[i][j] = getSimilarity(i, j);
				dist[j][i] = getSimilarity(j, i);
			}
		}
*/
/*
		for (int i = 0; i < n; i++)
		{
			for (int j = i+1; j < n; j++)
			{
				dist[i][j].clear();
				for (set<int>::iterator it = datas[j].begin(); it != datas[j].end(); it++)
				{
					if (datas[i].find(*it) != datas[i].end()) dist[i][j].insert(*it);
				}
			}
		}
		*/

		int res = INF;
		int total = 1 << (n-2);
		for (int mask = 0; mask < total; mask++)
		{
			int mask2 = mask * 4 + 2;
			char b[MAXN];
			for (int i = 0; i < n; i++)
			{
				b[i] = mask2 % 2;
				mask2 /= 2;
			}

			memset(ww,0,sizeof(ww));
			for (int i = 0; i < n; i++)
			{
				for (set<int>::iterator it = datas[i].begin(); it != datas[i].end(); it++)
				{
					ww[*it][(int)b[i]] = 1;
				}
			}

			int ans2 = 0;
			for (int i = 0; i < wordCount; i++)
			{
				if ((ww[i][0]) && (ww[i][1])) ans2++;
			}

/*
			ans.clear();
			for (int i = n-1; i >= 0; i--)
			{
				for (int j = i+1; j < n; j++)
				{
					if (b[i] != b[j])
					{
						for (set<int>::iterator it = dist[i][j].begin(); it != dist[i][j].end(); it++) ans.insert(*it);
					}
				}
			}
*/

			res = min(res, ans2);
		}

/*
		vector<int> e (n);
		vector<int> h (n);
		h[s] = n-1;
		vector < vector<int> > f (n, vector<int> (n));

		for (int i=0; i<n; ++i) {
			f[s][i] = c[s][i];
			f[i][s] = -f[s][i];
			e[i] = c[s][i];
		}

		vector<int> maxh (n);
		int sz = 0;
		for (;;) {
			if (!sz)
				for (int i=0; i<n; ++i)
					if (i != s && i != t && e[i] > 0) {
						if (sz && h[i] > h[maxh[0]])
							sz = 0;
						if (!sz || h[i] == h[maxh[0]])
							maxh[sz++] = i;
					}
			if (!sz)  break;
			while (sz) {
				int i = maxh[sz-1];
				bool pushed = false;
				for (int j=0; j<n && e[i]; ++j)
					if (c[i][j]-f[i][j] > 0 && h[i] == h[j]+1) {
						pushed = true;
						int addf = min (c[i][j]-f[i][j], e[i]);
						f[i][j] += addf,  f[j][i] -= addf;
						e[i] -= addf,  e[j] += addf;
						if (e[i] == 0)  --sz;
					}
				if (!pushed) {
					h[i] = INF;
					for (int j=0; j<n; ++j)
						if (c[i][j]-f[i][j] > 0 && h[j]+1 < h[i])
							h[i] = h[j]+1;
					if (h[i] > h[maxh[0]]) {
						sz = 0;
						break;
					}
				}
			}
		}
*/

		printf("Case #%d: %d\n",iT+1,res);
	}
	return 0;
}
