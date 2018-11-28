#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <stack>
using namespace std;

#define make(n) ll n;scanf("%lld",&n)
#define FOR(i,j,k) for(int i=j;i<k;i++)
#define FORD(i,j,k) for(int i=j-1;i>=k;i--)
#define pb push_back
#define mp make_pair
#define st first
#define nd second
#define ret return
#define ll long long
#define INF 2000000001
#define N 1000001
#define INFLL INF*INF
#define vi vector<int>
#define pii pair<int,int>

//stale

//struktury

//globalne
ll tab[]={1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004, 100000020000001};
//funckje

int main(){
	make(Z);

	FOR(dupa,1,Z+1){
		printf("Case #%d: ",dupa);
		
		make(a);make(b);

		int wyn=0;
		
		FOR(i,0,40)if(tab[i]>=a&&tab[i]<=b)wyn++;

		printf("%d\n",wyn);
	}
  ret 0;
}
