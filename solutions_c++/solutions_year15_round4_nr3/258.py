#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <cmath>

using namespace std;

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) 42
#endif

const int N = (int)1e3 + 10;
const int W = (int)1e5;
map <string, int> idByWord;
int listWords[N][N];
int cnt[N];
int typeLine[N];
int wordType[W];
int oldType[W];

int getId(string &str)
{
	int sz = idByWord.size();
	if (idByWord.find(str) == idByWord.end())
		idByWord[str] = sz;
	return idByWord[str];
}

void parseLine(string &str, int id)
{
	string word = "";
	for (int i = 0; i < (int)str.length(); i++)
	{
		if (str[i] == ' ')
		{
			if (word != "")
			{
				int w = getId(word);
				if (id < 2)
					wordType[w] |= (id + 1);
				listWords[id][cnt[id]++] = w;
			}
			word = "";
		}
		else
			word.push_back(str[i]);
	}
	if (word != "")
	{
		int w = getId(word);
		if (id < 2)
			wordType[w] |= (id + 1);
		listWords[id][cnt[id]++] = w;
	}
}

void solve()
{
	memset(cnt, 0, sizeof(cnt));
	for (int i = 0; i < W; i++)
		wordType[i] = oldType[i] = 0;

	idByWord.clear();
	int n;
	scanf("%d", &n);
	string str;
	getline(cin, str);
	for (int i = 0; i < 2; i++)
	{
		getline(cin, str);
		parseLine(str, i);
		typeLine[i] = i;
	}

	int ans = 0;
	for (int i = 0; i < (int)idByWord.size(); i++)
	{
		oldType[i] = wordType[i];
		if (wordType[i] == 3)
			ans++;
	}


	for (int i = 2; i < n; i++)
	{
		getline(cin, str);
		parseLine(str, i);
	}

	int bestAns = (int)1e9;
	for (int mask = 0; mask < (1 << (n - 2)); mask++)
	{
		int curAns = ans;
		for (int s = 0; s < n - 2; s++)
		{
			int id = s + 2;
			if (mask & (1 << s))
			{
				for (int q = 0; q < cnt[id]; q++)
				{
					int w = listWords[id][q];
					if (wordType[w] == -1)
						wordType[w] = oldType[w];
					if (wordType[w] != 3 && (wordType[w] | 1) == 3)
						curAns++;
					wordType[w] |= 1;
				}
			}
			else
			{
				for (int q = 0; q < cnt[id]; q++)
				{
					int w = listWords[id][q];
					if (wordType[w] == -1)
						wordType[w] = oldType[w];
					if (wordType[w] != 3 && (wordType[w] | 2) == 3)
						curAns++;
					wordType[w] |= 2;
				}
			}
		}
		for (int s = 2; s < n; s++)
		{
			for (int q = 0; q < cnt[s]; q++)
			{
				int w = listWords[s][q];
				wordType[w] = -1;
			}
		}
		bestAns = min(bestAns, curAns);
	}
	printf("%d\n", bestAns);
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		eprintf("%d\n", i);
		printf("Case #%d: ", i + 1);

		solve();
	}
	return 0;
}
