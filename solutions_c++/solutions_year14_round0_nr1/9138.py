#include <fstream>
#include <iomanip>
#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char* args[])
{
	ifstream fin(args[1]);
	ofstream fout(args[2]);	
	
	int n;
	fin >> n;
	for (int t = 1; t <= n; ++t)  {
		
		vector<bool> m(16, false);
		int r, k, res;
		fin >> r; --r;		
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j) {
				fin >> k; --k;
				if (i == r) m[k] = true;
			}
		int cnt = 0;
		fin >> r; --r;	
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j) {
				fin >> k; --k;
				if (i == r && m[k]) {
					 ++cnt;	res = k + 1;
				}
			}
		fout << "Case #" << t << ": ";
		if (cnt == 0) fout << "Volunteer cheated!" << endl;
		else if (cnt == 1) fout << res << endl;
		else fout << "Bad magician!" << endl;		
	}	
	
	fin.close();
	fout.close();
	return 0;
}
