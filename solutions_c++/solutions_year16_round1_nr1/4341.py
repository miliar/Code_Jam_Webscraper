#include <iostream>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <string>

using namespace std;
typedef long long LL;

int main(){
	FILE *fin = freopen("A-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	for(int t=1;t<=T;t++){
		string s;
		cin >> s;
		string res = "";
		if(s.size() > 0)
			res = s[0];
		for(int i=1;i<s.size();i++){
			if(s[i] >= res[0])
				res = s[i] + res;
			else
				res = res + s[i];
		}
		cout << "Case #" << t << ": ";
		cout << res << endl;
	}
}