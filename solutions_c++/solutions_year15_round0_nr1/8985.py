#include "fstream"
#include "iostream"
#include "string"
using namespace std;

int T;
int Smax;
string S;

int main() {
	int i;
	int case_t = 0;
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in", ios::in);
	fout.open("A-large.out", ios::out);
	fin >> T;
	while (T--) {
		case_t++;
		int ans = 0;
		int cnt = 0;
		fin >> Smax >> S;
		for (i = 0; i < S.length(); i++) {
			if (cnt < i) {
				ans += i - cnt;
				cnt = i;
			}
			cnt += S[i] - '0';
		}
		//printf("Case #%d: %d\n", case_t, ans);
		fout << "Case #" << case_t << ": " << ans << "\n";
	}
	fin.close();
	fout.close();
	return 0;
}