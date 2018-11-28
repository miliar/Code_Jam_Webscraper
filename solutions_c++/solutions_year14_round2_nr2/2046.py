/*ckpeteryu*/
#include<iostream>
#include<iomanip>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<climits>
#include<cmath>
#include<bitset>
#include<string>
#include<ctime>
#include<functional>
#include<map>
#include<set>
#include<vector>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define FOD(i,s,e) for(int i=(s);i>=(int)(e);i--)
#define FORVEC(i,a) for(int i=0;i<(int)((a).size());i++)
#define pb push_back
#define mp make_pair
#define CLR(s,x) memset(s,x,sizeof(s))
#define LL long long int
#define L long int

int main(int argc, char **argv){
		
	#ifndef GCJ		
		freopen("a1.txt","w",stdout);
		//freopen("a2.txt","w",stdout);
	#endif
	
	//ios_base::sync_with_stdio(false);
	
		
	int T,A,B,K;
	int cnt;
	scanf("%d",&T);
	FOR(k,0,T){
		cnt=0;
		scanf("%d%d%d",&A,&B,&K);
		FOR(i,0,A){
			FOR(j,0,B){
				if((i&j)<K){					
					cnt++;
				}
			}
		}
		printf("Case #%d: %d\n", k+1,cnt);
	}




	





		
	return 0;
}

//printf("Case #%d: No\n", i+1);