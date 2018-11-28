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

int t,n,m,primes[10000]={2,3,5,7};
long long init=0;
int num = 4;

char s[1001];

long long f1(int base, int to){
	long long x=1;
	for(int i=0;i<to;i++)
		x*=base;
	return x;
}

void gen(){
	int temp;
	for(int i=11;num<10000;i+=2){
		temp=1;
		for(int j=0;j<num&&primes[j]*primes[j]<=i;j++)
			if(i%primes[j]==0){ temp=0; break;}
		if(temp) primes[num++]=i;
	}
}

int check(ll x){
	for(int i=0;i<num&&primes[i]<x;i++){
		if(x%primes[i]==0)
			return primes[i];
	}
	return -1;
}

void con(long long x){
	int index=0;
	while(x>0)
		s[index++]=(x%2==1?'1':'0'), x/=2;
	for(int i=0;i<index/2;i++)
		swap(s[i],s[index-i-1]);
	s[index]='\0';
}

long long f2(int base){
	long long ans=0;
	for(int i=strlen(s)-1, j=0;i>=0;i--,j++)
		if(s[i]=='1')
			ans+=f1(base,j);
	return ans;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);
	vector<int> v1;
	gen();
	scanf("%d", &t);
	for(int z=1;z<=t;z++){
		scanf("%d %d", &n, &m);
		printf("Case #%d:\n", z);
		init=f1(2,n-1)+1;
		while(m>0){
			v1.clear();
			int succ=1;
			init+=2;
			con(init);
			for(int j=2;j<=10;j++)
				v1.push_back(check(f2(j)));

			for(int i=0;i<9;i++)
				if(v1[i]==-1){ succ=0; break;}
			if(succ){
				m--;
				printf("%s ", s);
				for(int i=0;i<9;i++)
					printf("%d ", v1[i]);
				putchar(10);
			}
		}
	}

	return 0;
}