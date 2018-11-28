#define _CRT_SECURE_NO_WARNINGS
#include<vector>
#include<unordered_map>
#include<unordered_set>
#include<set>
#include<iostream>
#include<math.h>
#include<algorithm>
#include<string>
#include<queue>
#include<stdint.h>
using namespace std;
typedef long long	ll;

void setDigit(ll sum, uint32_t &digits){
	while (sum){
		int d = sum % 10;
		sum = sum / 10;
		digits |= 1 << d;
	}
}
ll helperA(){
	int num = 0;
	cin >> num;
	if (!num) return -1;
	uint32_t digits = 0;
	ll sum = 0;
	while (digits != 0x3FF){
		sum += num;
		setDigit(sum, digits);
	}
	return sum;
}

//#define TEST
//#define SMALL
#define LARGE
int main(){
#ifdef TEST
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
#endif
#ifdef SMALL
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
#endif
#ifdef LARGE
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	int n = 0;
	cin >> n;
	string dump;
	getline(cin, dump);
	
	for (int i = 1; i <= n; i++){
		printf("Case #%d: ", i);
		ll ans = helperA();
		if (ans != -1)
			printf("%lld", ans);
		else
			printf("INSOMNIA");
		cout << endl;
	}
}