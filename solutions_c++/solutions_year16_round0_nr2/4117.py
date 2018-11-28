#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <iomanip>
#include <sstream>
#include <bitset>
#include <fstream>
#include <queue>
#include <math.h>
#include <set>
#include <stdlib.h>
#include <time.h>
#include <list>

#define For(i,a,b) for(int i=(a);i<(b);++i)
#define rep(i,n)  For(i,0,n)

//clear memory
#define CLR(a) memset((a), 0 ,sizeof(a))
#define check(a) rep(i, a.size()) cout << a[i] << endl
#define SORT(c) sort((c).begin(),(c).end())
#define ll long long
#define vi vector<int>
#define all(it,a) for(auto it = a.begin(); it!=a.end(); it++)
using namespace std;


int main(void) {
	int n;
	cin >> n;

	rep(i, n){
		string str;
		cin >> str;


		int leastpiv = -1;
		for (int k = str.length() - 1; k >= 0; k--) {
			if (str[k] == '-') {
				leastpiv = k;
				break;
			}
		}

		if (leastpiv == -1) {
			cout << "Case #" << (i + 1) << ": " << 0 << endl;
			continue;
		}
		char currentpiv = '-';
		int result = 1;
		for (int k = leastpiv; k >= 0; k--) {
			if (str[k] != currentpiv) {
				result++;
				currentpiv = str[k];
			}
		}


		cout << "Case #" << (i+1) << ": " << result << endl;
	}
	
	
	return 0;
}
