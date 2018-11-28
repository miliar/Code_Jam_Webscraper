#include <fstream>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;

char winner(char a, char b)
{
	if (a == 'R') return (b == 'S') ? a : b;
	if (a == 'S') return (b == 'P') ? a : b;
	if (a == 'P') return (b == 'R') ? a : b;
}

int main()
{
	ifstream 	f("in.txt");
	ofstream 	g("out.txt");
	int 		T, N, R, P, S;
	string 		letter("PRS");

	f >> T;
	for (int test = 1; test <= T; test++)
	{
		f >> N >> R >> P >> S;
		string ans = "IMPOSSIBLE";

		int maxOrder = 1;
		for (int i = 0; i < R + P + S; i++, maxOrder *= 3);
		for (int order = 0; order < maxOrder; order++)
		{
			string 	s(R + P + S, '*');
			int 	x  		= order;
			int 	cnt[] 	= {0, 0, 0};
			for (int i = s.length() - 1; i >= 0; i--)
			{
				s[i] = letter[x % 3];
				cnt[x % 3]++;
				x 	/= 3;
			}

			if (cnt[0] != P || cnt[1] != R || cnt[2] != S) continue;

			bool 	canFinish 	= true;
			string 	ss 			= s;
			int  	M 			= ss.length();
			for(int round = 0; round < N && canFinish; round++, M /= 2)
			{
				for (int i = 0; i < M/2; i++)
				{
					if (ss[2*i] == ss[2*i+1])
					{
						canFinish = false;
						break;
					}

					ss[i] = winner(ss[2*i], ss[2*i+1]);
				}
			}

			if (canFinish)
			{
				ans = s;
				break;
			}
		}

		g << "Case #" << test << ": " << ans << endl;
	}

	return 0;
}
