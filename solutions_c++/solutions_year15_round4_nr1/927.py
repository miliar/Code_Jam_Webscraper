#include <bits/stdc++.h>
using namespace std;

const int INF = 0x3f3f3f3f;

int R, C;

char mymap[105][105];
int LE[105], RE[105];
int up[105], down[105];

void init()
{
	memset(LE, 0, sizeof(LE));
	memset(RE, 0, sizeof(RE));
	memset(up, 0, sizeof(up));
	memset(down, 0, sizeof(down));
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);
	int T;
	cin >> T;
	for(int t = 1; t<=T; t++)
	{
		cin >> R >> C;
		for(int i=1; i<=R; i++)
			for(int j=1; j<=C; j++)
			{
				cin >> mymap[i][j];
			}

		init();

		for(int i=1; i<=R; i++)
		{
			for(int j=1; j<=C; j++)
				if(mymap[i][j] != '.')
				{
					if(LE[i] == 0) LE[i] = j;
					else LE[i] = min(LE[i], j);
					if(RE[i] == 0) RE[i] = j;
					else RE[i] = max(RE[i], j);
					if(up[j] == 0) up[j] = i;
					else up[j] = min(up[j], i);
					if(down[j] == 0) down[j] = i;
					else down[j] = max(down[j], i);
				}
		}

		int ans = 0;
		bool flag = true;
		for(int i=1; i<=R; i++)
		{
			for(int j=1; j<=C; j++)
			{
				//cerr << i << " " << j;
				//cerr << mymap[i][j] << " " << LE[i] << " " << RE[i] << " " << up[j] << " " << down[j] << endl;
				if(mymap[i][j] != '.' && LE[i] == j && RE[i] == j && up[j] == i && down[j] == i)
				{
					flag = false;
					goto next;
				}
				if(mymap[i][j] == '^' && up[j] == i) ans ++;
				if(mymap[i][j] == 'v' && down[j] == i) ans ++;
				if(mymap[i][j] == '<' && LE[i] == j) ans ++;
				if(mymap[i][j] == '>' && RE[i] == j) ans ++;
			}
		}

		next:;
		cout << "Case #" << t << ": ";
		if(!flag) cout << "IMPOSSIBLE" << endl;
		else cout << ans << endl;
	}

	return 0;
}
