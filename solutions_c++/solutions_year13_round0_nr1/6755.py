#include <iostream>
#include <fstream>

using namespace std;

main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.txt");
	int n;
	fin >> n;
	for (int cnt = 1; cnt <= n; ++cnt)
	{
		string v[4];
		string s = "Draw";
		for (int i = 0; i < 4; ++i)
			fin >> v[i];
		char ch[2] = {'O', 'X'};
		for (int c = 0; c <= 1; ++c)
		{
			char t = ch[c];
			for (int i = 0; i < 4; ++i)
			{
				int a = 0, b = 0;
				for (int j = 0; j < 4; ++j)
				{
					if (v[i][j] == t || v[i][j] == 'T')
						++a;
					if (v[j][i] == t || v[j][i] == 'T')
						++b;
				}
				if (a == 4 || b == 4)
				{
					s = t;
					s += " won";
					goto g;
				}
			}
			int a = 0, b = 0;
			for (int i = 0; i < 4; ++i)
			{
				if (v[i][i] == t || v[i][i] == 'T')
					++a;
				if (v[i][3-i] == t || v[i][3-i] == 'T')
					++b;
			}
			if (a == 4 || b == 4)
			{
				s = t;
				s += " won";
				goto g;
			}
		}
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				if (v[i][j] == '.')
				{
					s = "Game has not completed";
					goto g;
				}
			}
		}
		g:
		fout << "Case #" << cnt << ": " << s << endl << endl;
	}
}
