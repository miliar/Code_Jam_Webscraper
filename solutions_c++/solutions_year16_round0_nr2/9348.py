#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

int main(){
	FILE * fin, * fout;
	freopen_s(&fin, "B-large.in", "r", stdin);
	freopen_s(&fout, "pancakes.out", "w", stdout);

	int run, cnt; string line;
	cin >> run;
	for (int a = 1; a <= run; ++a){
		cin >> line;
		cnt = 0;
		for (int x = 0; x < line.length() - 1; ++x)
			if (line[x] != line[x+1]) ++cnt;
		if (line[line.length()-1] == '-') ++cnt;
		cout << "Case #" << a << ": " << cnt << endl;
	}
	return 0;
}
