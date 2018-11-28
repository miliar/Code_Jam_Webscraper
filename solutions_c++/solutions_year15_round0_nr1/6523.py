#include <iostream>
#include <cstdio>
#include <string>
#include <fstream>
using namespace std;

int t, n;
string s;

int main(){
	fstream fin("A.in");
	fstream fout("A.out");
	fin >> t;
	for(int ans, conut, i = 1; t--; ++i){
		ans = 0; conut = 0;
		fin >> n >> s;
		//cout << "look here: " << s << endl;
		for(int a = 0; a <= n; ++a){
			//cout << a << ": " << conut << endl;
			if(conut < a) ans += a - conut;
			conut = max(conut, a);
			conut += s[a] - '0';
		}
		fout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}
