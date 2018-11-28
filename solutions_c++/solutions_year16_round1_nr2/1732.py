#include <fstream>
#include <cstring>

using namespace std;

int main(){
	ifstream fin ("B-large.in");
	ofstream fout ("B-output.txt");
	int t, n, dat;
	fin >> t;
	int h[2501];
	for (int i = 1; i <= t; i++){
		fin >> n;
		fout << "Case #" << i << ":";
		memset(h, 0, 10004);
		for (int x = 0; x < n*2 - 1; x++){
			for (int y = 0; y < n; y++){
				fin >> dat;
				h[dat]++;
			}
		}
		for (int x = 1; x < 2501; x++){
			if (h[x]%2){
				fout << " " << x;
			}
		}
		fout << '\n';
	}
	return 0;
}
