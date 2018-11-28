#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int T;
int N,X;

void main()
{
	ifstream fin("A-large.in");
	ofstream fout("out.txt");
	fin >> T;
	for (int i = 0; i != T; i++)
	{
		fout << "Case #" << i+1 << ": ";
		fin >> N >> X;
		vector<int> S(N,0);
		for (int j = 0; j != N; j++)
			fin >> S[j];
		sort(S.begin(),S.end());
		int y = 0;
		int last = N-1;
		int first = 0;
		while(last > first)
		{
			if(S[last]+S[first] > X)
				last--;
			else
			{
				last--;first++;
			}
			y++;
		}
		if(last == first)
			y++;
		fout << y << endl;
	}
	fin.close();
	fout.close();
}