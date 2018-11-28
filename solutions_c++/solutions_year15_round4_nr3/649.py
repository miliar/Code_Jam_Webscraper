#include <stdio.h>
#include <map>
#include <vector>
#include <string>
using namespace std;

vector<int> w[212];
char s[112345];

bool tab[2][112345];

int
main(void)
{
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		int n, id  = 1;
		scanf("%d ", &n);
		map<string, int> hash;
		hash.clear();
		
		for(int i = 0 ; i < n; i++)
		{
			w[i].clear();
			fgets(s, 112345, stdin);
			string word;
			for(int j = 0; s[j] != '\0'; j++)
			{
				if(s[j] == ' ' || s[j] == '\n')
				{
					if(hash[word] == 0)
						hash[word] = id++;
					w[i].push_back(hash[word]);
					word.clear();
				}
				else
				{
					word += s[j];
				}
			}
		}
		
		int ans = 0x3f3f3f3f;
		for(int i = 0; i < (1 << (n-2)); i++)
		{
			for(int j = 1; j < id; j++)
				tab[0][j] = tab[1][j] = false;
			int tmp = 0;
			int mask = ((i << 2) | 1);
			for(int j = 0; j < n; j++)
				for(int k = 0; k < w[j].size(); k++)
					tab[(mask & (1 << j)) >> j][w[j][k]] = true;
			
			for(int j = 1; j < id; j++)
				if(tab[0][j] && tab[1][j])
					tmp++;
			ans = min(ans, tmp);
		}
		printf("Case #%d: %d\n", t, ans);
	}
}






















