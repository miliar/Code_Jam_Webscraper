#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <string>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <fstream>

using namespace std;

int INF = 1E9;

int main() {
	freopen("A-large.in", "r", stdin);
	ofstream fout;
	fout.open("answer.out");

	int T;
	cin>>T;

	for(int Case = 1; Case <= T; Case++){
		fout<<"Case #"<<Case<<": ";
		//fout<<endl;
		string s;
		cin>>s;
		string res = "";
		char cur = ' ';
		for(int i = 0; i < s.length(); i++){
			if(s[i] >= cur){
				res = string(1,s[i]) + res;
				cur = s[i];
			}else
				res += s[i];
		}
		fout<<res<<endl;
		

		//fout<<endl;
	}
	return 0;
}
