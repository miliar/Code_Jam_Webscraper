#include <cstdio>
#include <vector>
#include <utility>
#include <cstring>
#include <cstdlib>
#include <map>
#include <iostream>
#include <algorithm>
#include <string>
#include <stack>
#include <queue>
#include <cmath>
#include <set>
#include <assert.h>
#include <bitset>

using namespace std;
#define pb push_back
#define mp make_pair
#define S second
#define F first
#define INF 0x3f3f3f3f
#define ll long long
#define mod 10
#define B 33
#define MAX (int)10e6

typedef vector<int> vi;
typedef pair<int,int>ii;
typedef vector<ii> vii;
typedef unsigned long long hash;


typedef struct bignum bignum;

// struct bignum{
// 	string n;

// 	bignum operator *(bignum &a) const{
// 		for(int i=a.n.size()-1; i>=0; --i){
// 			for(int j=n.size(); j>=0; --j){

// 			}
// 		}
// 	}
// };
int n;
ll x,y;
char v[200];
bool check(ll a){
	sprintf(v,"%lld",a);
	int tam = strlen(v);
	for(int i=0 , j=tam-1; i < j; ++i,--j){
		// printf("i: %c,  j:%c\n",v[j],v[k]);
		if(v[i] != v[j]) return false;
	}
	return true;
}
int main (int argc,char *argv[]){
	scanf("%d",&n);
	for(int cases=1; cases<=n; ++cases){
		scanf("%lld %lld",&x,&y);

		ll sum = 0;
		ll fat = 0;
		ll i = 0;
		do{
			i++;
			if(!check(i)) continue;
			fat = i*i;
			if(fat < x) continue;
			if(fat > y) break;
			// printf("fat: %lld\n",fat);
			
			if(check(fat)) sum++;
		}while(fat <= y);
		printf("Case #%d: %lld\n",cases,sum);
	}
	return 0;
}