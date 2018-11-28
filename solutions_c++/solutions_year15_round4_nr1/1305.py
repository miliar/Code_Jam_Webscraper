#include <fstream>

using namespace std;

ifstream fin ("A.in");
ofstream fout ("A.out");

int T;
int N, M;
char Map[1000][1000];
int s = 0;

int main ()
{
	fin >> T;
	for (int t = 1; t <= T; t++)
	{
		s = 0;
		fin >> N >> M;
		for (int i = 1; i <= N; i++)
			for (int j = 1; j <= M; j++)
				fin >> Map[i][j];
		for (int i = 1; i <= N; i++)
			for (int j = 1; j <= M; j++)
			{
				if (Map[i][j] == '.') continue;
				int mx, my;
				if (Map[i][j] == '^') {mx = -1; my = 0;}
				if (Map[i][j] == '>') {mx = 0; my = 1;}
				if (Map[i][j] == 'v') {mx = 1; my = 0;}
				if (Map[i][j] == '<') {mx = 0; my = -1;}
				int x = i + mx, y = j + my;
				while (x > 0 && y > 0 && x <= N && y <= M)
				{
					if (Map[x][y] != '.') goto ed;
					x += mx; y += my;
				}
				for (int k = 1; k <= N; k++)
					if (k != i && Map[k][j] != '.')
					{
						s++;
						goto ed;
					}
				for (int k = 1; k <= M; k++)
					if (k != j && Map[i][k] != '.')
					{
						s++;
						goto ed;
					}
				fout << "Case #" << t << ": IMPOSSIBLE" << endl;
				goto ed1;
				ed:;
			}
		fout << "Case #" << t << ": " << s << endl;
		ed1:;
	}
}
