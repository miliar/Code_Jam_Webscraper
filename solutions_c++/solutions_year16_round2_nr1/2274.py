#include <iostream>
#include <tuple>
#include <sstream>
#include <vector>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>

#define mp make_pair
#define mt make_tuple
#define fi first
#define se second
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define forn(i, n) for (int i(0); i < (int)(n); ++i)
#define for1(i, n) for (int i(1); i < (int)(n); ++i)
#define ford(i, n) for (int i((int)(n)); i >= 0; --i)
#define fore(i, a, b) for (int i((int)(a)), i <= (int)(b); ++i)

using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef	vector<pii> vpi;
typedef	vector<vi> vvi;
typedef long long i64;
typedef vector<i64> vi64;
typedef vector<vi64> vvi64;
typedef pair<i64, i64> pi64;
typedef double ld;

int main(){
	ofstream output;
	output.open("output.txt");
	ifstream input;
	input.open("A-large.in");

	int T(0);
	string in;
	vector<int> letters, numbers;
	letters.resize(26);
	numbers.resize(10);
		
	input >> T;

	forn(i, T){
		input >> in;
		forn(j, letters.size())
			letters[j] = 0;
		forn(j, numbers.size())
			numbers[j] = 0;
		forn(j, in.size()){
			letters[in[j] - 65] += 1;
		}
		if (letters[25] > 0) {
			numbers[0] += (letters[25]);
			letters[4] -= (letters[25]);
			letters[17] -= (letters[25]);
			letters[14] -= (letters[25]);
			letters[25] = 0;
		}
		if (letters[22] > 0) {
			numbers[2] += letters[22];
			letters[19] -= letters[22];
			letters[14] -= letters[22];
			letters[22] = 0;
		}
		if (letters[23]) {
			numbers[6] += letters[23];
			letters[18] -= letters[23];
			letters[8] -= letters[23];
			letters[23] = 0;
		}
		if (letters[6] > 0) {
			numbers[8] += letters[6];
			letters[4] -= letters[6];
			letters[8] -= letters[6];
			letters[7] -= letters[6];
			letters[19] -= letters[6];
			letters[6] = 0;
		}
		if (letters[18] > 0) {
			numbers[7] += letters[18];
			letters[4] -= (letters[18] * 2);
			letters[21] -= letters[18];
			letters[13] -= letters[18];
			letters[18] = 0;
		}
		if (letters[21] > 0) {
			numbers[5] += letters[21];
			letters[8] -= letters[21];
			letters[5] -= letters[21];
			letters[4] -= letters[21];
			letters[21] = 0;
		}
		if (letters[5] > 0) {
			numbers[4] += letters[5];
			letters[14] -= letters[5];
			letters[20] -= letters[5];
			letters[17] -= letters[5];
			letters[5] = 0;
		}
		if (letters[14] > 0) {
			numbers[1] += letters[14];
			letters[13] -= letters[14];
			letters[4] -= letters[14];
			letters[14] = 0;
		}
		if (letters[19] > 0) {
			numbers[3] += letters[19];
			letters[7] -= letters[19];
			letters[17] -= letters[19];
			letters[4] -= (letters[19] * 2);
			letters[19] = 0;
		}
		if (letters[8] > 0) {
			numbers[9] += letters[8];
			letters[13] -= (letters[8] * 2);
			letters[4] -= letters[8];
			letters[8] = 0;
		}
		output << "Case #" << i + 1 << ": ";
		forn(j, numbers.size()) {
			while (numbers[j] > 0) {
				output << j;
				numbers[j] -= 1;
			}
		}
		output << endl;
	}

	return 0;
}

