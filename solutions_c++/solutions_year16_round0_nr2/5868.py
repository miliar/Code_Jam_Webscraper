/*
 * new
 *      Author: AbdullaAshraf
 */
#include<bits/stdc++.h>
using namespace std;
const int OO = 1000000000;
const int maxn = 1e5 + 5;

typedef long long ll;
#define REP(i,n) for(int(i)=0; (i)<(n); (i)++)

string pan;

void flip(int x) {
	REP(i,x){
		if (pan[i] == '+') pan[i] = '-';
		else pan[i] = '+';
	}
}

int main(void) {
	ofstream sout ("output.txt");
	ifstream sin ("B-large.in");
	int T;
	sin >> T;
	REP(i,T)
	{
		int c=0;
		sin >> pan;
		for (int i=pan.size()-1; i>=0; i--){
			if (pan[i] == '-'){
				c++;
				flip(i);
			}
		}
		sout << "Case #" << i+1 << ": " << c;
		if (i!=T-1) sout << endl;
	}
	return 0;
}
