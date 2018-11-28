#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <map>
#include <queue>
#include <deque>
#include <vector>
#include <cstdlib>
#include <utility>
#include<iostream>
#include <iterator>
#include <set>
typedef long long ll;
#define fi first
#define se second
#define PB(a) push_back(a);
#define INF = 1000000000;
#define REP(i,n) for (int i = 0; i < n; i++)
#define REPI(i,n) for (int i = 1; i <= n; i++)
#define REPN(i,n) for (int i = n-1; i >= 0; i--)
#define REPF(j,i,n) for (int j = i; j < n; j++)
#define OPENR(a) freopen(a,"r",stdin)
#define OPENW(a) freopen(a,"w",stdout)
//int gcd(int a,int b){ return b == 0 ? a : gcd(b,a%b);}
//int lcm(int a,int b){ return a * (b/gcd(a,b)); }


using namespace std;

int n;
int main (){
	OPENR("A-large.in");
	OPENW("out_large.txt");
	scanf("%d",&n);
	for(int i=0;i<n;i++){
		int person;
		char str[1005];
		scanf("%d %s",&person,str);
		int temp = 0;
		int tambah = 0;
		for(int j=0;j<strlen(str);j++){
			if(j > temp){
				tambah += (j - temp);
				temp += (j- temp);
			}
			temp += str[j] - '0';
		}
		printf("Case #%d: %d\n",i+1,tambah);
	}
	
}
