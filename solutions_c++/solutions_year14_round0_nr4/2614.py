#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <iostream>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <list>
#include <utility>
#include <bitset>
using namespace std;

int GCD (int a, int b ) {
	if ( a==0 ) return b;
	return GCD ( b%a, a );
}

#define CetakInt(J) printf("Cetak %d\n",J);
#define CetakChar(J) printf("%c\n",J);
#define sf scanf
#define pf printf
#define FOR(a,b,c) for(int a = b; a<=c ; a++)
#define FOR1(a,b,c) for(int a = b; a<c; a++)

typedef long long int int64;

bool dsc (int i,int j) { 
	return (i>j); 
}

int main(){
	int T;
	scanf("%d",&T);
	for (int i = 1; i <= T; ++i) {
		int N;
		scanf("%d",&N);
		vector<double> vnaomi;
		vector<double> vken;
		for (int j = 1; j <= N; ++j) {
			double x;
			cin >> x;
			vnaomi.push_back(x);
		}
		sort(vnaomi.begin(), vnaomi.end());
		
		for (int j = 1; j <= N; ++j) {
			double x;
			cin >> x;
			vken.push_back(x);
		}
		sort(vken.begin(), vken.end());
		
		/*kalau bohong*/
		int cntbohong = 0;
		vector<double> vnaomibohong = vnaomi;
		vector<double> vkenbohong = vken;
		do {
			if (vnaomibohong.front() < vkenbohong.front()) {
				vnaomibohong.erase(vnaomibohong.begin());
			} else {
				vnaomibohong.erase(vnaomibohong.begin());
				vkenbohong.erase(vkenbohong.begin());
				++cntbohong;
			}
		} while (!vnaomibohong.empty());
		
		
		/*kalau tidak bohong*/
		do {
			double depannaomi = vnaomi.front();
			do {
				double depanken = vken.front();
				vken.erase(vken.begin());
				if (depanken < depannaomi) {
					//do nothing
				} else {
					vnaomi.erase(vnaomi.begin());
					break;
				}
			} while (!vken.empty());
		} while (!vken.empty());
		printf("Case #%d: %d %d\n",i,cntbohong,vnaomi.size());
	}
	return 0;
}