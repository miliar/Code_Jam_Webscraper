#include <iostream>
#include <fstream>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <queue>
#include <utility>
using namespace std;

ifstream fin ("A.in");
ofstream fout ("A.out");
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef long long ll;
typedef vector<ll> vll;
typedef vector<vll> vvll;
#define pb push_back
#define sz(a) int((a).size())
#define all(c) (c).begin(),(c).end()
#define abs(x) ((x)<0 ? -(x) : (x))

int main() {
	int c, T, i, j;
	fin >> T;
	vvi cards;
	int vol;
	bool cheated;
	int ammpos;
	int sol;
	vi pos;
	for (c = 1; c <= T; c++) {
		cards.resize(4, vi(4, 0));
		fin >> vol;
		for (i = 0; i < 4; i++) {
			for (j = 0; j < 4; j++) {
				fin >> cards[i][j];
			}
		}
		pos = cards[vol-1];
		fin >> vol;
		for (i = 0; i < 4; i++) {
			for (j = 0; j < 4; j++) {
				fin >> cards[i][j];
			}
		}
		ammpos = 0;
		for (i = 0; i < 4; i++) {
			for (j = 0; j < 4; j++) {
				if (pos[i] == cards[vol-1][j]){
					ammpos++;
					sol = pos[i];
				}
			}
		}
		if (ammpos == 0) {
			fout << "Case #" << c << ": Volunteer cheated!" << endl;
		}
		else if (ammpos == 1){
			fout << "Case #" << c << ": " << sol << endl;
		}
		else {
			fout << "Case #" << c << ": Bad magician!" << endl;
		}


		pos.clear();
		cards.clear();
	}
}
