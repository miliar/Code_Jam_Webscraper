#include <iostream>
#include <string>

using namespace std;

int main () {
	int N;
	cin >> N;
	for (int n=0;n<N;++n) {
		int chars[26];
		for (int i=0;i<26;++i) {
			chars[i] = 0;
		}
		string line;
		cin >> line;
		int letters = line.length();
		for (int i=0;i<letters;++i) {
			chars[(int)(line[i]-'A')]++;
		}
		int result[10];
		for (int i=0;i<10;++i) {
			result[i] = 0;
		}
		if (chars[(int)('Z'-'A')]>0) {
			int zeroes = chars[(int)('Z'-'A')];
			chars[(int)('Z'-'A')] = 0;
			chars[(int)('E'-'A')] -= zeroes;
			chars[(int)('R'-'A')] -= zeroes;
			chars[(int)('O'-'A')] -= zeroes;
			result[0] = zeroes;
		} 
		if (chars[(int)('X'-'A')]>0) {
			int sixes = chars[(int)('X'-'A')];
			chars[(int)('X'-'A')] = 0;
			chars[(int)('S'-'A')] -= sixes;
			chars[(int)('I'-'A')] -= sixes;
			result[6] = sixes;
		}
		if (chars[(int)('W'-'A')]>0) {
			int twoes = chars[(int)('W'-'A')];
			chars[(int)('W'-'A')] = 0;
			chars[(int)('T'-'A')] -= twoes;
			chars[(int)('O'-'A')] -= twoes;
			result[2] = twoes;
		}
		if (chars[(int)('G'-'A')]>0) {
			int eights = chars[(int)('G'-'A')];
			chars[(int)('G'-'A')] = 0;
			chars[(int)('E'-'A')] -= eights;
			chars[(int)('I'-'A')] -= eights;
			chars[(int)('H'-'A')] -= eights;
			chars[(int)('T'-'A')] -= eights;
			result[8] = eights;
		}
		if (chars[(int)('S'-'A')]>0) {
			int sevens = chars[(int)('S'-'A')];
			chars[(int)('S'-'A')] = 0;
			chars[(int)('E'-'A')] -= 2*sevens;
			chars[(int)('V'-'A')] -= sevens;
			chars[(int)('N'-'A')] -= sevens;
			result[7] = sevens;
		}
		if (chars[(int)('V'-'A')]>0) {
			int fives = chars[(int)('V'-'A')];
			chars[(int)('V'-'A')] = 0;
			chars[(int)('F'-'A')] -= fives;
			chars[(int)('I'-'A')] -= fives;
			chars[(int)('E'-'A')] -= fives;
			result[5] = fives;
		}
		if (chars[(int)('U'-'A')]>0) {
			int fours = chars[(int)('U'-'A')];
			chars[(int)('U'-'A')] = 0;
			chars[(int)('F'-'A')] -= fours;
			chars[(int)('O'-'A')] -= fours;
			chars[(int)('R'-'A')] -= fours;
			result[4] = fours;
		}
		if (chars[(int)('O'-'A')]>0) {
			int ones = chars[(int)('O'-'A')];
			chars[(int)('O'-'A')] = 0;
			chars[(int)('N'-'A')] -= ones;
			chars[(int)('E'-'A')] -= ones;
			result[1] = ones;
		}
		if (chars[(int)('N'-'A')]>0) {
			int nines = chars[(int)('N'-'A')] / 2;
			chars[(int)('N'-'A')] = 0;
			chars[(int)('I'-'A')] -= nines;
			chars[(int)('E'-'A')] -= nines;
			result[9] = nines;
		}
		if (chars[(int)('H'-'A')]>0) {
			int threes = chars[(int)('H'-'A')];
//				chars[(int)('H'-'A')] = 0;
//				chars[(int)('I'-'A')] -= threes;
//				chars[(int)('E'-'A')] -= threes;
			result[3] = threes;
		}
		string outline = "";
		for (int i=0;i<10;++i) {
			for (int k=0;k<result[i];++k) {
				outline += (char)('0'+i);
			}
		}
		cout << "Case #" << n+1 << ": " << outline << endl;
	}
	return 0;
}
