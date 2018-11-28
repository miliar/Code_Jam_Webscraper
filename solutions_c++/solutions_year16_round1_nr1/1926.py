#include <iostream> 
#include <fstream>
#include <vector>
#include <queue>
#include <cstring>
#include <string>
#include <algorithm>
#include <stack>
#include <functional>
#include "stdlib.h" 
#include "time.h"
#include <set>
#include <map>
#include <numeric>

#define INF 800
using namespace std;
#define LL long long



int main() {
#ifdef __ACM
	ifstream fin("A-large (1).in");	streambuf *cinbackup;  	cinbackup = cin.rdbuf(fin.rdbuf());
#endif
	int cas = 1;
	int T;
	cin >> T;
	while (T--) {
		string S;
		cin >> S;
		string before = S.substr(0, 1);
		for (int i = 1; i < S.size(); i++)
		{
			char c = S[i];
			int putbefore = c - before[0];
			int putafter = c - before[before.size() - 1];
			if (c <= before[before.size() - 1]) {
				before = before + c;
			}
			else if(c >= before[0]) {
				before = c + before;
			}
			else {
				before = before + c;
			}
		}
		cout << "Case #" << cas << ": " << before << endl;
		cas++;
	}
#ifdef __ACM
	system("pause");
#endif
}

