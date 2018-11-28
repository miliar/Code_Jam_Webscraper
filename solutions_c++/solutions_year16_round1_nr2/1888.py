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
	ifstream fin("B-large (1).in");	streambuf *cinbackup;  	cinbackup = cin.rdbuf(fin.rdbuf());
#endif
	int cas = 1;
	int T;
	cin >> T;
	while (T--) {
		int N;
		cin >> N;
		map<int, int> m;
		for (int i = 0; i < 2 * N  * N - N; i++)
		{
			int k;
			cin >> k;
			map<int, int>::iterator mit;;
			mit = m.find(k);
			if (mit == m.end())
				m[k] = 1;
			else
				m[k] += 1;
		}
		vector<int> v;
		map<int, int>::iterator it = m.begin();
		for (; it != m.end(); ++it) {
			if (it->second % 2 == 1) {
				v.push_back(it->first);
			}
		}
		sort(v.begin(), v.end());

		cout << "Case #" << cas << ":";
		for (int i = 0; i < v.size(); i++)
		{
			cout << " " << v[i];
		}
		cout << endl;
		cas++;
	}
#ifdef __ACM
	system("pause");
#endif
	return 0;
}

