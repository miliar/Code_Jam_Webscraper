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

int main() {  
	freopen("in.txt", "r", stdin);
	freopen("ans.txt", "w", stdout);
	
	int T;
	cin >> T;
	for(int t=1; t<=T; t++) {
		long long k, c, s;
		cin >> k >> c >> s;
		cout << "Case #" << t << ": ";
		long long p = 1;
		for(int i=1; i<c; i++)
			p = p * k;
		for(int i=1; i<=s; i++) {
			cout << p * i << " ";
		}
		cout << endl;
	}
	
	return 0;
}