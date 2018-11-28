#include <fstream>
#include <vector>
#include <queue>
#include <algorithm>
#include <functional>

using namespace std;

int table[1001][1001];

void preculc(){
	for (int i = 1; i <= 1000; ++i)
	for (int j = 1; j <= 1000; ++j){
		if (i <= j) table[i][j] = 1;
		else{
			int l = max(table[i - 1][j], 2);
			while ((i / l + (i % l ? 1 : 0)) > j) ++l;
			table[i][j] = l;
		}
	}
}

int main(){
	ios_base::sync_with_stdio(false);
	preculc();
	ifstream inf("B-large.in");
	ofstream outf("output.txt");
	vector<int> a;
	int t, d;
	inf >> t;
	for (int k = 0; k < t; ++k){
		int ans = 1000;
		inf >> d; 
		a.resize(d);
		for (int i = 0; i < d; ++i) inf >> a[i];
		for (int i = 1; i <= 1000; ++i){
			int tans = i;
			for (int j = 0; j < (int)a.size(); ++j) tans += table[a[j]][i] - 1;
			ans = min(tans, ans);
		}
		outf << "Case #" << k + 1 << ": " <<  ans << '\n';
	}
}