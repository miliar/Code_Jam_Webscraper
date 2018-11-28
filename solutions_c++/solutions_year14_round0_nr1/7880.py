#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <cstdio>
#include <cstring>
#include <deque>
#include <queue>

using namespace std;

#if defined WIN32
#define scanf scanf_s
#endif

int main()
{
	ifstream fin("small.txt");
	ofstream fout("result.txt");
	int a[4][4], b[4][4];
	int f, s;
	int t;
	fin >> t;
	int index = 0;
	while (t--)
	{
		fin >> f;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				fin >> a[i][j];
		fin >> s;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				fin >> b[i][j];
		f--, s--;

		
			

		int cnt = 0;
		int ans;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				if (a[f][i] == b[s][j])
					cnt++, ans = a[f][i];
		if (cnt == 1)
			fout << "Case #" << ++index << ": " << ans << endl;
		else if (cnt < 1)
			fout << "Case #" << ++index << ": " << "Volunteer cheated!" << endl;
		else 
			fout << "Case #" << ++index << ": " << "Bad magician!" << endl;
	}
	return 0;
}