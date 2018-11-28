#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>
#include <string>
#include <set>
#include <cctype>
#include <stack>
#include <queue>
#include <map>
#include <set>

using namespace std;

int main(){
	freopen("a.in", "r", stdin);
	freopen("aa.out", "w", stdout);
	int T, maxi, sofar, need;
	string s;
	cin >> T;
	
	for(int i = 0; i < T; i++) {
		cin >> maxi >> s;
		sofar = 0;
		need = 0;
		
		for(int j = 0; j < maxi + 1; j++) {
			if (sofar < j) {
				need += j - sofar;
				sofar = j;
			}
			sofar += (s[j] - '0');
		}
		cout << "Case #" << (i+1) << ": " << need << "\n";
	}
	
	return 0;
}
