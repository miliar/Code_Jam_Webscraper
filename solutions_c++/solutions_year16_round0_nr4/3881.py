#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <complex>
#include <sstream>
#include <iostream>
#include <iomanip>

using namespace std;

template<class T> inline T sqr(T x) { return x*x; }

typedef long long ll;//int(4バイト)は2×10^9程度まで %llu （intとlongは同じ）

#define REP(i,n) for (int i=0;i<(n);i++) //for書いた方が速いか？

#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(),(a).rend()
#define PB push_back
#define MP make_pair
#define SORT(c) sort((c).begin(),(c).end())//コンテナのみ 配列のソートはsort(array,array+N)
#define CLR(a) memset((a), 0 ,sizeof(a)) //1byte単位 コンテナはfill

const double PI = acos(-1.0);
/*int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};*/

int main() {
	/*テストケース変数*/
	int Test;
	scanf("%d", &Test);
	/*繰り返す時の変数初期化忘れに気を付ける*/
	for (int Case = 1; Case <= Test; Case++){
		int k,c,s;
		scanf("%d %d %d",&k, &c, &s); //文字が入力の場合は%*cによる数字の後に残る改行の読み捨て必要かも 読み捨てるのに変数はいらない
		if(c == 1) {
			if(s < k) {
				printf("Case #%d: IMPOSSIBLE\n", Case);
			} else {
				printf("Case #%d:", Case);
				for(int i = 1; i <= k; i++) printf(" %d", i);
				printf("\n");			
			}
			continue;
		}
		if(s < (k / 2) + 1) {
			printf("Case #%d: IMPOSSIBLE\n", Case);
			continue;
		}
		else {
			ll l = 1;
			for(int i = 0; i < c; i++) l *= k;
			printf("Case #%d:", Case);
			for(int i = 1; i <= (k / 2) + 1; i++) printf(" %llu", (l / k) * i - (i - 1));
			printf("\n");
		}
	}
	return 0;
}