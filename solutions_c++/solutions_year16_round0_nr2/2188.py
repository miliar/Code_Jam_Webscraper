#include <cstdio>
#include <vector>
#include <iostream>
#include <string>
using namespace std;
FILE *fi = freopen("B-large.in", "r", stdin);
FILE *fo = freopen("BLout.txt", "w", stdout);
#define ll long long
string str;
int test;
int main(){
	scanf("%d", &test);
	int lev = 0;
	while (test--){
		++lev;
		cin >> str;
		int cnt = 0;
		for (int i = 1; i < str.size(); i++){
			if (str[i] != str[i - 1])++cnt;
		}
		if (str.back() == '-')++cnt;
		printf("Case #%d: %d\n", lev, cnt);
	}
}