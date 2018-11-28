#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<ctime>
using namespace std;
#define FOR(i,s,e) for (int i=s;i<e;i++)
#define FOE(i,s,e) for (int i=s;i<=e;i++)
#define FOD(i,s,e) for (int i=s;i>=e;i--)
#define SET(a,e) memset(a,e,sizeof(a))
#define LL long long
#define pb push_back

int T,X,R,C;

int main () {
	
	scanf("%d",&T);
	
	FOE(tc,1,T) {
		scanf("%d%d%d",&X,&R,&C);
		printf("Case #%d: ",tc);
		
		if (X==1) printf("GABRIEL\n");
		else if (X==2) {
			if (R*C%2==1) printf("RICHARD\n");
			else printf("GABRIEL\n");
		}
		else if (X==3) {
			if (R*C%3==0 && (R>=3 || C>=3) && R>=2 && C>=2) printf("GABRIEL\n");
			else printf("RICHARD\n"); 
		}
		else if (X==4) {
			if (R*C%4==0 && (R>=4 || C>=4) && R>=3 && C>=3) printf("GABRIEL\n");
			else printf("RICHARD\n"); 
		}
	}
	
	return 0;
}

