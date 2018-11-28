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

typedef long long LL;//int(4バイト)は2×10^9程度まで %llu （intとlongは同じ）

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

LL convert(LL x,int n) {
	LL result = 0;
	LL b = 1;
	while(x > 0){
		result += (x % 2) * b;
		x /= 2;
		b *= n;
	}
	return result;
}

string convert2(LL x){
	string binary;
	while(x > 0){
		if(x % 2 == 0) binary.insert(0,"0");
		if(x % 2 == 1) binary.insert(0,"1");
		x /= 2;
	}
	return binary;
}

int main() {
	/*テストケース変数*/
	int Test;
	scanf("%d", &Test);
	/*繰り返す時の変数初期化忘れに気を付ける*/
	for (int Case = 1; Case <= Test; Case++){
		printf("Case #%d:\n",Case);
		int n,j;
		scanf("%d %d",&n,&j); //文字が入力の場合は%*cによる数字の後に残る改行の読み捨て必要かも 読み捨てるのに変数はいらない
		LL i = 1;
		for(int a = 0; a < n/2 - 1; a++) i *= 2;
		LL imax = i * 2;
		i++;
		int count = 0;
		for(; i < imax; i+=2){
			cout << convert2(i) << convert2(i) << ' ' <<  convert(i,2) << ' ' << convert(i,3) << ' ' << convert(i,4) << ' ' << convert(i,5) << ' ' << convert(i,6) << ' ' << convert(i,7) << ' ' << convert(i,8) << ' ' << convert(i,9) << ' ' << convert(i,10) << endl;
			count++;
			if(count == j) break;
		}
	}
	return 0;
}