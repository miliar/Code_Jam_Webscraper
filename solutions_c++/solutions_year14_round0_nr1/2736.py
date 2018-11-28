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
	
	int T,n,t,cnt,ans;
	int a[17];	
	scanf("%d",&T);
	FOR(k,0,T){
		cnt = ans = 0;
		scanf("%d",&n);
		fill(a,a+17,0);		
		FOR(i,0,4){
			FOR(j,0,4){
				scanf("%d",&t);
				if(i==n-1) a[t]=1;
			}
		}
		scanf("%d",&n);		
		FOR(i,0,4){
			FOR(j,0,4){
				scanf("%d",&t);
				if(i==n-1){
					if(a[t]){ cnt++; ans=t;}
				}
			}
		}
		if(cnt==1) printf("Case #%d: %d\n",k+1,ans);
		else if(!cnt) printf("Case #%d: Volunteer cheated!\n",k+1);
		else printf("Case #%d: Bad magician!\n",k+1);
	}
		
	return 0;
}

//printf("Case #%d: No\n", i+1);