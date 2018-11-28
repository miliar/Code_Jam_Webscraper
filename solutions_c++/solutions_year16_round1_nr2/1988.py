#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <deque>
#define maxN 50+5


using namespace std;

int a[2*maxN][maxN];
int n;

int cauta(int x){
	int k = 0;
	for (int i = 0; i < 2 * n - 1; ++i){
		for (int j = 0; j < n; ++j)
			if (a[i][j] == x)
				k++;
	}
	if (k % 2 == 0)
		return 1;
	return 0;
}

int main(){
	ifstream f("date.in");
	ofstream g("date.out");

	int T;
	f >> T;
	for (int t = 1; t <= T; ++t){
		vector <int> S;
		f >> n;

		for (int i = 0; i < 2*n - 1; ++i)
			for (int j = 0; j < n; ++j)
				f >> a[i][j];
		
		for (int i = 0; i < 2 * n - 1; ++i)
			for (int j = 0; j < n; ++j)
				if (cauta(a[i][j]) == 0)
					S.push_back(a[i][j]);

		sort(S.begin(), S.end());

		g << "Case #" << t << ": ";
		g << S[0] << " ";
		for (int j = 1; j < S.size(); ++j)
			if (S[j] != S[j - 1])
				g << S[j] << " ";
		g << "\n";
	}

	f.close();
	g.close();

	return 0;
}