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

int t,n,a[10];

int poss(int x){
	while(x>0)
		a[x%10]=1,x/=10;
	for(int i=0;i<=9;i++)
		if(a[i]==0)
			return 0;
	return 1;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);

	scanf("%d", &t);
	for(int z=1;z<=t;z++){
		printf("Case #%d: ", z);
		scanf("%d", &n),memset(a,0,sizeof(a));
		if(n==0) printf("INSOMNIA\n");
		else {
			for(int i=1;;i++)
				if(poss(i*n)){
					printf("%d\n", i*n);
					break;
				}
		}
	}

	return 0;
}