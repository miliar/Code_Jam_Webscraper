#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;
int a[10], b[30];

int main(){
	ifstream f("date.in");
	ofstream g("date.out");

	int d[10] = { 0, 2, 6, 4, 5, 3, 7, 8, 9, 1 };
	vector<string>V{"ZERO", "TWO", "SIX", "FOUR", "FIVE", "THREE", "SEVEN", "EIGHT", "NINE", "ONE" };

	int T;
	f >> T;

	for (int t = 1; t <= T; ++t){
		string s;
		f >> s;
		for (int i = 0; i < s.size(); ++i)
			b[s[i] - 'A']++;

		for (int i = 0; i <= 9; ++i){
			int ok = 1;
			while (ok){
				int j;

				for (j = 0; j < V[i].size() && ok; ++j){
					if (!b[V[i][j] - 'A']) ok = 0;
					b[V[i][j] - 'A']--;
				}

				if (ok)a[d[i]]++;
				for (int k = 0; ok == 0 && k < j; k++)
					b[V[i][k] - 'A']++;
			}
		}

		g << "Case #" << t << ": ";
		for (int i = 0; i <= 9; ++i)
			while (a[i]){
				g << i;
				a[i]--;
			}
		g << "\n";

		for (int i = 0; i < 30; ++i)
			b[i] = 0;
	}

	return 0;
}