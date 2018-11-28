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
#include <math.h>

#define INF 800
using namespace std;
#define LL long long

#define G 0
#define L 1


int main() {
#ifdef __ACM
	ifstream fin("D-small-attempt0.in");	streambuf *cinbackup;  	cinbackup = cin.rdbuf(fin.rdbuf());
#endif
	int cas = 1;
	int T;
	cin >> T;
	while (T--) {
		LL K, C, S;
		cin >> K >> C >> S;
				
		cout << "Case #" << cas << ":";
		for (LL i = 1; i <= K; i++)
		{
			cout << " " << i;
		}
		cout << endl;
		cas++;
	}
#ifdef __ACM
	system("pause");
#endif
}

