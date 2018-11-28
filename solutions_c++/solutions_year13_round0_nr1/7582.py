#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <string>
#include <set>
#include <stack>
#include <deque>
#include <map>
#include <cmath>
#include <vector>
#include <iostream>
#include <cctype>
#include <algorithm>
using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int tst;
	cin >> tst;
	for (int t=0;t<tst;t++)
	{
		vector<string> mas(4);
		pair<int,int> st(-1,-1);
		for (int i=0;i<4;i++)
		{
			cin >> mas[i];
			
			for (int j=0;j<4;j++)
				if (mas[i][j] == 'T')
					st = make_pair(i,j);

		}

		cout << "Case #" << (t + 1) << ": ";

		char ans = 0;
		for (int i=0;!ans && i<2;i++)
		{
			char c = (i==0?'X':'O');
			if (st.first != -1)
			mas[st.first][st.second] = c;

			for (int i=0;!ans && i<4;i++)
			{
				if (mas[i][0] == c && mas[i][1] == c && mas[i][2] == c && mas[i][3] == c|| 
					mas[0][i] == c && mas[1][i] == c && mas[2][i] == c && mas[3][i] == c)
					ans = c;
			}

			if (mas[0][0] == c && mas[1][1] == c && mas[2][2] == c && mas[3][3] == c)
				ans = c;
			if (mas[0][3] == c && mas[1][2] == c && mas[2][1] == c && mas[3][0] == c)
				ans = c;
		}
		if (ans)
		{
			cout << ans << " won\n";
			continue;
		}

		int cnt = 0;
		for (int i=0;i<4;i++)
			cnt += count(mas[i].begin(), mas[i].end(), '.');

		if (cnt == 0)
			cout << "Draw\n";
		else
			cout << "Game has not completed\n";
	}
	return 0;
}