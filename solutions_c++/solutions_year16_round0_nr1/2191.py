#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;
ifstream fin("1.in");
ofstream fout("1.out");

int main() {
	int T; fin >> T;
	for (int rk = 1; rk <= T; rk ++) {
		int st; fin >> st;
		int count = 1; 
		bool visited[10] = {0};
		if (st == 0) {
			fout << "Case #" << rk << ": INSOMNIA" << endl;
			continue;
		}
		while ( true ) {
			int num = count * st;
			while ( num ) {
				visited[num % 10] = 1;
				num /= 10;
			}
			int t = 0;
			for (int i = 0; i < 10; i ++)
				t += visited[i];
			if (t == 10) break;
			count ++;
		}
		fout << "Case #" << rk << ": " << count * st << endl;
	}
	fout.close();
	return 0;
}
