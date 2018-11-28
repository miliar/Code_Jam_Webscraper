
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <climits>
#include <ctime>
using namespace std;
int count_c(string s, int a, char c){
	int i = a, ret = 0;
	while(s[i] == c && i < s.size()) {ret++;i++;}
	return ret;
}

int main() {
	long int a, b, T;
	cin >> T;
	int cse = 1;
	while(cse <= T){
		string s;
		cin >> s;
		int a =0, b = 0;
		int flip = 0;
		a = a + count_c(s,a,'+');
		while(a < s.length()){
			a = a + count_c(s,a,'+');
			b = count_c(s,a,'-');
			if(a > 0) flip += 1;
			if(b > 0) flip += 1;
			a = a + b;
			a = a + count_c(s,a,'+');
		}
		cout << "Case #" << cse << ": " << flip << "\n";
		cse++;
	}
    return 0;
}
