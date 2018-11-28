#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <stdexcept>
#include <functional>
#include <math.h>
#include <utility>
#include <sstream>
#pragma comment(linker, "/STACK:133217728")

using namespace std;
int cnt[47];
int c = 0;

void f(int n) {
	while(n > 0) {
		int p = n % 10;
		n /= 10;
		if(++cnt[p] == 1) c++;
	}
}
int main() {  
	freopen("in.txt", "r", stdin);
	freopen("ans.txt", "w", stdout);
	int T;
	cin >> T;
	for(int t=1; t<=T; t++) {
		int n;
		cin >> n;

		cout << "Case #" << t << ": ";
		if(!n) {
			cout << "INSOMNIA" << endl;
			continue;
		}
		for(int i=0; i<10; i++) cnt[i] = 0;
		c = 0;
		int k = 0;
		while(c != 10) {
			k += n;
			f(k);
		}
		cout << k << endl;
	}
	return 0;
}