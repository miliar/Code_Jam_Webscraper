#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
#define trans for(int i=0;i<4;++i)for(int j=0;j<4;++j)
#define CHK(str) { \
	sort(str.begin(), str.end()); \
	if(str[3] == 'Z') str[3] = str[0]; \
	if(str == "XXXX") return 1; \
	if(str == "OOOO") return 0; \
} 

class Board {
private:
	char data[4][4];
public:
	void read(istream& is) { 
		trans {
			is>>data[i][j];
			if(data[i][j] == 'T') data[i][j] = 'Z';
		} 
	}
	int empties() { int re=0; trans if(data[i][j]=='.') re++; return re; }
	int status() {
		string d1, d2;
		for(int i=0;i<4;++i){
			string r, c;
			d1 += data[i][i];
			d2 += data[i][3-i];
			for(int j=0; j<4; ++j) {
				r += data[i][j];
				c += data[j][i];
			}
			// cout << r << " " << c << endl;0
			CHK(r)
			CHK(c)
		}
		// cout << d1 << " " << d2 << endl;
		CHK(d1)
		CHK(d2)
		return -1;
	}
};
int main() {
	int cases, casn = 1;
	cin >> cases;
	Board bd;
	while(cases--) {
		
		bd.read(cin);
		int stat = bd.status();

		cout << "Case #" << casn++ << ": ";
		if(stat == -1) {
			if(!bd.empties())
				cout << "Draw";
			else
				cout << "Game has not completed";
		}
		else if(stat)
			cout << "X won";
		else
			cout << "O won";

		cout << endl;
	}
	return 0;
}
