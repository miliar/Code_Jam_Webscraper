#include <iostream>
#include <iomanip>
#include <climits>
#include <stack>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <cassert>

#define FOR(i,n) for(int i=0,_n=n;i<_n;i++)
#define FORR(i,s,n) for(int i=s,_n=n;i<_n;i++)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define pli pair<ll,int>
#define vi vector<int>
#define fs first
#define sec second

#define maxn 100000

using namespace std;
typedef long long ll;

const ll MOD = 1000000007LL;

int d[27];
char st[27];
int nuc[27];

void solve(int prim){
	int n;
	scanf("%d",&n);
	FOR(i,n){
		scanf("%s",st);
		d[i]=0;
		FOR(j,n)if(st[j]=='1')d[i]|=(1<<j);
	}
	int rez=0;
	if(n==1){
		if(d[0]==0)rez=1;
		printf("Case #%d: %d\n",prim, rez);
		return;
	}
	if(n==2){
		sort(d,d+2);
		if(d[1]==3)rez=__builtin_popcount(3-d[0]);
		if(d[1]==2){
			if(d[0]==2)rez=2;
			if(d[0]==0)rez=1;
		}
		if(d[1]==1){
			if(d[0]==1)rez=2;
			else rez=1;
		}
		if(d[1]==0)rez=2;
		printf("Case #%d: %d\n",prim, rez);
		return;
	}
	if(n==3){
		int best=n*n;
		FORR(i,1,(1<<n)){
			FORR(j,1,(1<<n)){
				FORR(k,1,(1<<n)){
					int aa[3]={i,j,k};
					if((i&d[0])!=d[0])continue;
					if((j&d[1])!=d[1])continue;
					if((k&d[2])!=d[2])continue;
					FOR(i1,n)nuc[i1]=0;
					FOR(i1,n){
						FOR(i2,n){
							if(aa[i1]&(1<<i2))nuc[i2]=1;
						}
					}
					if(nuc[0]==0 || nuc[1]==0 || nuc[2]==0)continue;
					int ok =1;
					FOR(i1,n){
						int st=0;
						FOR(i2,n){
							if((aa[i1]&aa[i2])==0)continue;
							if(aa[i1]!=aa[i2])ok=0;
							else st++;
						}
						if(st!=__builtin_popcount(aa[i1]))ok=0;
					}
					if(ok==0)continue;
					int cena=0;
					cena+=__builtin_popcount(i-d[0]);
					cena+=__builtin_popcount(j-d[1]);
					cena+=__builtin_popcount(k-d[2]);
					if(cena<best)best=cena;
				}
			}
		}
		printf("Case #%d: %d\n",prim, best);
		return;
	}
	if(n==4){
		int best=n*n;
		FORR(i,1,(1<<n)){
			FORR(j,1,(1<<n)){
				FORR(k,1,(1<<n)){
					FORR(l,1,(1<<n)){
						int aa[4]={i,j,k,l};
						if((i&d[0])!=d[0])continue;
						if((j&d[1])!=d[1])continue;
						if((k&d[2])!=d[2])continue;
						if((l&d[3])!=d[3])continue;
						FOR(i1,n)nuc[i1]=0;
						FOR(i1,n){
							FOR(i2,n){
								if(aa[i1]&(1<<i2))nuc[i2]=1;
							}
						}
						if(nuc[0]==0 || nuc[1]==0 || nuc[2]==0||nuc[3]==0)continue;
						int ok =1;
						FOR(i1,n){
							int st=0;
							FOR(i2,n){
								if((aa[i1]&aa[i2])==0)continue;
								if(aa[i1]!=aa[i2])ok=0;
								else st++;
							}
							if(st!=__builtin_popcount(aa[i1]))ok=0;
						}
						if(ok==0)continue;
						int cena=0;
						cena+=__builtin_popcount(i-d[0]);
						cena+=__builtin_popcount(j-d[1]);
						cena+=__builtin_popcount(k-d[2]);
						cena+=__builtin_popcount(l-d[3]);
						if(cena<best)best=cena;
					}
				}
			}
		}
		printf("Case #%d: %d\n",prim, best);
		return;
	}
}

int main(){
	int n;
	scanf("%d",&n);
	FORR(i,1,n+1)solve(i);
	return 0;
}
