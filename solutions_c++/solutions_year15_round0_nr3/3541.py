#include <fstream>
#include <string>

using namespace std;

ifstream fin("C-small-attempt0.in");
ofstream fout("out.txt");

int main() {
	int tests;
	fin >> tests;
	int l, x;
	string s, seq, ans;
	int res[5][5];
	res[1][1] = 1; res[1][2] = 2; res[1][3] = 3; res[1][4] = 4;
	res[2][1] = 2; res[2][2] = -1; res[2][3] = 4; res[2][4] = -3;
	res[3][1] = 3; res[3][2] = -4; res[3][3] = -1; res[3][4] = 2;
	res[4][1] = 4; res[4][2] = 3; res[4][3] = -2; res[4][4] = -1;
	for(int test = 0; test < tests; ++test) {
		fin >> l >> x;
        fin >> seq;
		s = "";
		for(int i = 0; i < x; ++i) {
			s += seq;
		}
		bool flag = false;
		int is = 1;
		for(int i = 0; i < s.length() - 2 && !flag; ++i) {
			int x = s[i] - 'i' + 2;
			if(is > 0) {
				is = res[is][x];
			} else {
				is = res[-is][x];
				is *= -1;
			}
			if(is == 2) {
				int js = s[i + 1] - 'i' + 2, ks = 1;
				for(int i2 = i + 2; i2 < s.length(); ++i2) {
					int x = s[i2] - 'i' + 2;
			        if(ks > 0) {
				        ks = res[ks][x];
			        } else {
				        ks = res[-ks][x];
				        ks *= -1;
			        }
				}
				if(js == 3 && ks == 4) {
				  	flag = true;
				}
			    for(int j = i + 2; j < s.length() - 1 && !flag; ++j) {
				    int x = s[j] - 'i' + 2;
			        if(js > 0) {
				        js = res[js][x];
			        } else {
				        js = res[-js][x];
				        js *= -1;
			        }
					if(ks > 0) {
				        ks = res[x][ks];
						ks *= -1;
			        } else {
				        ks = res[x][-ks];
					}

				    if(js == 3 && ks == 4) {
				    	flag = true;
				    }
			    }
			}
		}
		if(flag) {
			ans = "YES";
		} else {
			ans = "NO";
		}
		fout << "Case #" << test + 1 << ": " << ans << endl;
	}
	return 0;
}
