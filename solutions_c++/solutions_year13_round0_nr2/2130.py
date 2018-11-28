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

#define make(n) int n;scanf("%d",&n)
#define FOR(i,j,k) for(int i=j;i<k;i++)
#define FORD(i,j,k) for(int i=j-1;i>=k;i--)
#define pb push_back
#define mp make_pair
#define st first
#define nd second
#define ret return
#define ll long long
#define INF 2000000001
#define N 101
#define INFLL INF*INF
#define vi vector<int>
#define pii pair<int,int>

//stale

//struktury

//globalne
int tab[N][N];
int PION[N];
int POZ[N];
//funckje
bool check(int n,int m){
	FORD(h,101,1){
		FOR(i,0,n){
			FOR(j,0,m){
				if(tab[i][j]==h){
					if(PION[i]==-1)PION[i]=h;
					if(POZ[j]==-1)POZ[j]=h;

					if(PION[i]!=h&&POZ[j]!=h)ret 0;
				}
			}
		}
	}

	ret 1;
	
}

int main(){
	make(Z);

	FOR(dupa,1,Z+1){
		printf("Case #%d: ",dupa);

		FOR(i,0,N)PION[i]=POZ[i]=-1;

		make(n);make(m);

		FOR(i,0,n)
			FOR(j,0,m)
				scanf("%d",&tab[i][j]);

		if(check(n,m))printf("YES\n");
		else printf("NO\n");
	}

  ret 0;
}
