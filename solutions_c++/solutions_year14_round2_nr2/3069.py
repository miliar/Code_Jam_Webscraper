#include <cstdio>
#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <utility>
#define VAR(i,v) auto i = (v)
#define SIZE(x) ((int)(x).size())
#define ALL(x) (x).begin(), (x).end()
#define REP(i,b) for(int i=0; i<(b); ++i)
#define FOR(i,a,b) for(int i=(a); i<=(b); ++i)
#define FORD(i,a,b) for(int i=(a); i>=(b); --i)
#define FOREACH(i,c) for(VAR(i,(c).begin()); i != (c).end(); ++i)
#define PB push_back
#define MP make_pair
#define ST first
#define ND second

using namespace std;
typedef vector<int> VI;
typedef long long LL;

const int MAXT = 100;
const int MAXA = 1000;
int t;

string DecToBin(int number) {
	if (number == 0) return "0";
	if (number == 1) return "1";
	if (number%2==0) return DecToBin(number/2) + "0";
	else return DecToBin(number/2) + "1";
}

int BinToDec(string number) {
	int result = 0, pow = 1;
	for(int i = SIZE(number)-1; i>=0; --i, pow<<=1) result += (number[i]-'0') * pow;
	return result;
}

int main() {
	scanf("%d", &t);
	REP(i,t) {
		int c, d, k;
		scanf("%d%d%d", &c, &d, &k);

		int ret = 0;
		
		REP(a,c) {
			REP(b,d) {
		
				string ba = DecToBin(a);
				string bb = DecToBin(b);

				while(SIZE(ba) != SIZE(bb)) {
					if (SIZE(ba) < SIZE(bb)) {
						ba = "0" + ba;
					} else if (SIZE(ba) > SIZE(bb)) {
						bb = "0" + bb;
					}
				}

				VI out_tmp(SIZE(ba));
				REP(i,SIZE(ba)) if (ba[i]=='1' && bb[i]=='1') out_tmp[i] = 1; else out_tmp[i] = 0;
		
				string out = "";
				REP(i,SIZE(ba)) out += (out_tmp[i]==1) ? '1' : '0';

				int nmb = BinToDec(out);

				if (nmb < k) ret++;

				//cout << ba << " " << bb << " " << out <<  " " << ret << endl;
			}
		}

		cout << "Case #" << i+1 << ": " << ret << endl;
	}
	
	return 0;
}
