#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <ctime>
using namespace std;
typedef long long LL; 
typedef pair<int, int> PII;
typedef vector<int> VI;
#define PB push_back
#define MP make_pair
#define FOR(i, n) for(int i = 0; i < (n); i++)
#define REP(i, a, b) for(int i = (a); i <= (b); i++)
#define CLR(x, a) memset(x, a, sizeof(x))
//#define L(x) ((x) << 1)
#define R(x) (((x) << 1) + 1)
#define LB(x) ((x)&(-(x)))
#define SL(x) (1 << (x))
#define X first
#define Y second
const int MAXN = 5;

LL palindromes[] = {
	1, 4, 9, 121, 484, 676, 10201, 12321, 14641, 40804, 44944, 69696, 94249, 698896, 1002001, 1234321, 4008004, 5221225, 6948496, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 522808225, 617323716, 942060249, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 637832238736, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1086078706801, 1210024200121, 1212225222121, 1214428244121, 1230127210321, 1232346432321, 1234567654321, 1615108015161, 4000008000004, 4004009004004, 4051154511504, 5265533355625, 9420645460249, 100000020000001, 100220141022001, 102012040210201, 102234363432201, 121000242000121, 121242363242121, 123212464212321, 123456787654321, 123862676268321, 144678292876441, 165551171155561, 400000080000004, 900075181570009
};

bool check(LL n){
	int num = 0;
	int bits[15];
	while(n){
		bits[num ++] = n % 10;;
		n /= 10;
	}
	for(int i = 0; i < num / 2; i ++){
		if(bits[i] != bits[num - 1 - i])return false;
	}
	return true;
}

int main(){
	// cout << check(0) << ", " << check(1) << ", " << check(10) << ", " << check(11) << ", " << check(101) << endl;
	// cout << sizeof(palindromes) << " " << palindromes[67] << endl;
	int T; cin >> T;
	FOR(cas, T){
		printf("Case #%d: ", cas + 1);
		int res = 0;
		LL A, B;
		cin >> A >> B;
		for(int i = 0; ; i ++){
			if(palindromes[i] >= A && palindromes[i] <= B){
				LL root = sqrt(palindromes[i]);
				if(check(root))res ++;
			}
			if(palindromes[i] > B)break;
		}
		cout << res << endl;
	}
}