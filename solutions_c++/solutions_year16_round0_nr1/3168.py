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
	ifstream fin("A-large.in");	streambuf *cinbackup;  	cinbackup = cin.rdbuf(fin.rdbuf());
#endif
	int cas = 1;
	int T;
	char used[10];
	//scanf("%d", &T);
	cin >> T;
	while (T--) {
		LL x;
		cin >> x;
		//scanf("%lld", &x);
		LL t = 0;
		bool suc = false;
		memset(used, 0, 10 * sizeof(char));
		for (int trytimes = 0; trytimes < INF; trytimes++)
		{
			t += x;
			LL part = t;
			while (part) {
				used[part % 10] = 1;
				part /= 10;
			}
			for (int i = 0; i < 10; i++)
			{
				if (!used[i]) {
					goto CONTINUE;
				}
			}
			suc = true;
			cout << "Case #" << cas << ": " << t <<  endl;
			//printf("Case #%d: %lld\n", cas, t);
			break;
		CONTINUE:
			continue;
		}
		if (!suc) {
			cout << "Case #" << cas << ": INSOMNIA" << endl;
			//printf("Case #%d: INSOMNIA\n", cas);
		}
		cas++;
	}
#ifdef __ACM
	system("pause");
#endif
}

