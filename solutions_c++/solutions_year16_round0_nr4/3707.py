#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main(){
	ifstream f("date.in");
	ofstream g("date.out");

	int T;
	f >> T;

	for (int t = 1; t <= T; ++t){
		int s, c, k;
		f >> k >> c >> s;

		g << "Case #" << t << ": ";
		for (int i = 1; i <= s; ++i)
			g << i << " ";
		g << "\n";
	}

	f.close();
	g.close();

	return 0;
}
