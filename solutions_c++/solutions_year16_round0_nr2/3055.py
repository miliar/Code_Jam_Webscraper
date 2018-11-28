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
#include<bitset>
using namespace std;
typedef long long	ll;


//int helperB(bitset<128> &s){
//	string str;
//	getline(cin, str);
//	string dump;
//	getline(cin, dump);
//	int n = str.size();
//	for (int i = 0; i < n; i++){
//		if (str[i] == '+'){
//			s.set(i);
//		}
//		else{
//			s.reset(i);
//		}
//	}
//	int ans = 0;
//	int i = n - 1;
//	while (i >= 0){
//		if (!s[i]){
//			ans += 1;
//			s.flip();
//		}
//		i--;
//	}
//	return ans;
//}
int helperB(){
	string str;
	getline(cin, str);
	
	int n = str.size();
	
	int ans = 0;
	int i = n - 1;
	while (i >= 0){
		if ((str[i] == '+' && ans%2) || (str[i] == '-' && (ans % 2==0))){
			ans += 1;
		}
		i--;
	}
	return ans;
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
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
#endif
#ifdef LARGE
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
#endif
	int n = 0;
	cin >> n;
	string dump;
	getline(cin, dump);
	//bitset<128> s;
	for (int i = 1; i <= n; i++){
		printf("Case #%d: ", i);
		printf("%d", helperB());
		cout << endl;
	}
}