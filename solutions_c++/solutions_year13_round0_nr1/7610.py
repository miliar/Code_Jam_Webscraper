#include <vector>
#include <fstream>
#include <sstream>
#include <iostream>
using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;++i)
#define REP(i,n) FOR(i,0,n)
typedef vector<string> VS;

int main() {
	int z, qz;
	cin>>z;
	ofstream myfile;
	myfile.open ("C:\\Users\\Raaja\\Desktop\\test.txt");
	VS ret;
	ret.push_back("X won");
	ret.push_back("O won");
	ret.push_back("Draw");
	for(qz = 1; qz <= z ; qz++) {
		VS a;
		int val = -1;
		REP(i,4) {
			string s;
			cin>>s;
			a.push_back(s);
		}
		ret.pop_back();
		REP(i,4)REP(j,4)
			if(a[i][j] == '.') {
				i=j=5;
				ret.push_back("Game has not completed");
			}
		if(ret.size() == 2)
			ret.push_back("Draw");
		REP(i,4) {
			char k;
			if(a[i][0] == 'X' || a[i][0] == 'O')
				k=a[i][0];
			else if(a[i][0] == 'T' && (a[i][1] == 'X' || a[i][1] == 'O'))
				k=a[i][1];
			else
				continue;
			val = 3;
			FOR(j,1,4) {
				if(a[i][j] != 'T' && a[i][j] != k) {
					val = -1;
					break;
				}
			}
			if(val != -1) {
				val = (k=='X')?0:1;
				break;
			}
		}
		if(val != 0 && val != 1)
			REP(i,4) {
				char k;
				if(a[0][i] == 'X' || a[0][i] == 'O')
					k=a[0][i];
				else if(a[0][i] == 'T' && (a[1][i] == 'X' || a[1][i] == 'O'))
					k=a[1][i];
				else
					continue;
				val = 3;
				FOR(j,1,4) {
					if(a[j][i] != 'T' && a[j][i] != k) {
						val = -1;
						break;
					}
				}
				if(val != -1) {
					val = (k=='X')?0:1;
					break;
				}
			}
		if(val != 0 && val != 1) {
			char k = 0;
			if(a[0][0] == 'X' || a[0][0] == 'O')
				k=a[0][0];
			else if(a[0][0] == 'T' && (a[1][1] == 'X' || a[1][1] == 'O'))
				k=a[1][1];
			val = 3;
			if(k!=0)
				FOR(i,1,4) {
					if(a[i][i] != 'T' && a[i][i] != k) {
						val = -1;
						break;
					}
				}
			if(val != -1 && k) {
				val = (k=='X')?0:1;
			}
		}
		if(val != 0 && val != 1) {
			char k = 0;
			if(a[3][0] == 'X' || a[3][0] == 'O')
				k=a[3][0];
			else if(a[3][0] == 'T' && (a[2][1] == 'X' || a[2][1] == 'O'))
				k=a[2][1];
			val = 3;
			if(k!=0)
				FOR(i,1,4) {
					if(a[3-i][i] != 'T' && a[3-i][i] != k) {
						val = -1;
						break;
					}
				}
			if(val != -1 && k) {
				val = (k=='X')?0:1;
			}
		}
		if(val != 0 && val != 1) val = 2;
		myfile<<"Case #"<<qz<<": "<<ret[val]<<endl;
	}
	myfile.close();
}
