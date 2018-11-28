#include <cstdio>
#include <iostream>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <string.h>
#include <cmath>
#include <sstream>
#include <map>
#include <bitset>
#include <cstdlib>
#include <cstring>
#include <set>
#include <ctype.h>
#include <string>
using namespace std;

typedef long long ll;
typedef vector<int> vi;


int main(){
#ifndef ONLINE_JUDGE
	//freopen("in.in", "r", stdin);
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
#endif
	int t, L, x, cc=1;
	cin >> t;
	map<char, int> sym;
	sym['1'] = 0;	sym['i'] = 1;
	sym['j'] = 2;	sym['k'] = 3;

	sym['+'] = 0;	sym['-'] = 1;

	char mp[4][4] = {
		{'1', 'i', 'j', 'k'},
		{'i', '1', 'k', 'j'},
		{'j', 'k', '1', 'i'},
		{'k', 'j', 'i', '1'}
	};
	char sign[4][4] = {
		{'+', '+', '+', '+'},
		{'+', '-', '+', '-'},
		{'+', '-', '-', '+'},
		{'+', '+', '-', '-'}
	};
	char mpSing[2][2] = {
		{'+', '-'},
		{'-', '+'}
	};
	while(t--){
		bool ans = false;
		string s = "", str="";
		cin >> L >> x >> s;
		for (int i = 0; i < x; i++){
			str += s;
		}
		L = str.length();
		int stage = 0;
		char pre = str[0];
		char preSig = '+';
		for (int i = 1; i < L; i++){
			if(pre == '1'){
				pre = str[i];
			}else if( (stage == 0 && pre == 'i') ||
				(stage == 1 && pre == 'j') ||
				(stage == 2 && pre == 'k') ){
				pre = str[i];
				stage++;
			}else{
				char res =   mp[ sym[pre] ][ sym[str[i]] ];
				char sig = sign[ sym[pre] ][ sym[str[i]] ];
				preSig = mpSing[ sym[preSig] ][ sym[sig] ];
				pre = res;
			}
			//printf("pre= %c, preSig= %c, stage=%d\n", pre, preSig, stage);
		}
		ans = (stage==3 && preSig=='+' && pre=='1') || (stage==2 && preSig=='+' && pre=='k');
		printf("Case #%d: %s\n", cc++, ans ? "YES" : "NO");
	}
	return 0;
}