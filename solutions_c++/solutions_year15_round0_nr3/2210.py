#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <unordered_map>
using namespace std;

#define RAW_MUL(x, y) (((x)<<7) + ((((x) >= 0)? 1:-1)*(y)))
#define MUL(x, y) (pT[(RAW_MUL((x), (y)))])

unordered_map<int, int> pT;
int main() {
	pT[49] = 49;		pT[105] = 105;		pT[106] = 106;		pT[107] = 107;
	pT[-49] = -49;		pT[-105] = -105;	pT[-106] = -106;	pT[-107] = -107;

	pT[6321] = 49;		pT[6377] = 105;		pT[6378] = 106;		pT[6379] = 107;
	pT[13489] = 105;	pT[13545] = -49;	pT[13546] = 107;	pT[13547] = -106;
	pT[13617] = 106;	pT[13673] = -107;	pT[13674] = -49;	pT[13675] = 105;
	pT[13745] = 107;	pT[13801] = 106;	pT[13802] = -105;	pT[13803] = -49;
	pT[-6321] = -49;	pT[-6377] = -105;	pT[-6378] = -106;	pT[-6379] = -107;
	pT[-13489] = -105;	pT[-13545] = 49;	pT[-13546] = -107;	pT[-13547] = 106;
	pT[-13617] = -106;	pT[-13673] = 107;	pT[-13674] = 49;	pT[-13675] = -105;
	pT[-13745] = -107;	pT[-13801] = -106;	pT[-13802] = 105;	pT[-13803] = 49;

	int T;
	cin >> T;
	int target[3] = {105, 107, -49};
	for (int t = 1; t <= T; t++) {
		int L, X;
		string s;
		cin >> L >> X;
		cin >> s;

		int c = 0;
		int targetCount = 0;
		for (int x = 0; x < X; x++) {
			for (int l = 0; l < L; l++) {
				c = MUL(c, s[l]);
				if (targetCount <= 1 && c == target[targetCount]) {
					targetCount++;
				}
			}
		}
		string result = (targetCount == 2 && c == -49) ? "YES" : "NO";
		cout << "Case #" << t << ": " << result << endl;
	}

	return 0;
}
