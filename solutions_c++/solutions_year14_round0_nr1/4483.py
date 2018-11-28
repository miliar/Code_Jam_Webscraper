#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>

using namespace std;

ifstream in("me.txt");
ofstream out("ans.txt");

int main()
{
	int T; in >> T;
	for (int cc = 1; cc <= T; ++cc)
	{
		int pos[4] = {0}; int ans = 0, fin = 0;
		in >> ans;
		for (int i = 0; i < 16; ++i)
		{
			int num; in >> num;
			if (i/4 == ans-1)
				pos[i%4] = num;
		}
		in >> ans;
		for (int i = 0; i < 16; ++i)
		{
			int num; in >> num;
			if (i/4 == ans-1)
			{
				for (int j = 0; j < 4 && fin != -1; ++j)
					if (num == pos[j])
					{
						if (fin == 0) fin = num;
						else fin = -1;
					}
			}
		}
		out << "Case #" << cc << ": ";
		if (fin == -1) out << "Bad magician!\n";
		else if (fin == 0) out << "Volunteer cheated!\n";
		else out << fin << "\n";
	}
}