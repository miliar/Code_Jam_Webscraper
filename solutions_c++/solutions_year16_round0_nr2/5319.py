#define _CRT_SECURE_NO_WARNINGS

//#pragma comment(linker, "/STACK:268435456")
#ifdef _MSC_VER
#	include <intrin.h>
#	define __builtin_popcount(n) __popcnt(n)
#endif

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
#include <list>
#include <functional>
#include <map>
#include <string>
#include <set>
#include <vector>
#include <cmath>
#include <bitset>
#define ll long long
#define ull unsigned ll
#define pll pair<ll, ll>
#define pii pair<int, int>
#define vi vector<int>
#define vll vector<ll>
#define PI acos(-1.0L)
#define inf 0x3f3f3f3f
#define inf2 0x3f3f3f3f3f3f3f3f
// [Note1: Use long double]

using namespace std;

int t,ans;
char s[1001];

void flip(int i){
	if(s[i]=='+') s[i]='-';
	else s[i]='+';
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);
	
	scanf("%d", &t);
	for(int z=1;z<=t;z++){
		int ans=0;
		scanf("%s", s);
		int last=-1;
		for(int i=strlen(s)-1;i>=0;i--)
			if(s[i]=='-'){
				last=i;
				break;
			}
		while(last!=-1){
			int temp;
			if(s[0]=='-') temp=last;
			else {
				for(int i=0;i<last;i++)
					if(s[i]=='+') temp=i;
					else break;
			}

			for(int i=0;i<=temp/2;i++){
				swap(s[i],s[temp-i]),flip(i),flip(temp-i);
				if(temp-i==i) flip(i);
			}


			last = -1;
			for (int i = strlen(s) - 1; i >= 0; i--)
				if (s[i] == '-') {
					last = i;
					break;
				}
			ans++;
		}
		printf("Case #%d: %d\n", z, ans);
	}



	//system("pause");
	return 0;
}