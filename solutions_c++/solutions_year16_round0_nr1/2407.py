#include <iostream>
#include <fstream>
using namespace std;
bool finded[10];
int main() {
	int t;	cin >> t;
	ofstream ofs("out.txt");
	for (int i = 1; i <= t; i++) {
		int n;	cin >> n;
		ofs << "Case #" << i << ": ";
		if (n == 0) {
			ofs << "INSOMNIA" << endl;
			continue;
		}
		for (int i = 0; i < 10; i++)	finded[i] = false;
		int cur = n;
		while (true) {
			int tmp = cur;
			while (tmp) {
				finded[tmp % 10] = true;
				tmp /= 10;
			}
			bool end = true;
			for (int i = 0; i < 10; i++)	if (!finded[i])	end = false;
			if (end)	break;
			else	cur += n;
		}
		ofs << cur << endl;
	}
	return 0;
}