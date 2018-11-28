#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>

#define FOR(A,B,C) for(int A=B;A<C;A++)
#define EFOR(A,B,C) for(int A=B;A<=C;A++)
#define RFOR(A,B,C) for(int A=B;A>=C;A--)
#define MEM(A,B) memset(A,B,sizeof(A))
#define ALL(A) A.begin(),A.end()
#define SZ(A) int(A.size())
#define LL long long

using namespace std;

int brd[101][101];
int rwMx[101][101],clMx[101][101];
int R,C;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	int T;
	scanf("%d",&T);

	EFOR(cs,1,T){
		scanf("%d%d",&R,&C);
		FOR(rw,0,R)		FOR(cl,0,C)
			scanf("%d",&brd[rw][cl]);

		printf("Case #%d: ",cs);

		FOR(rw,0,R){
			int tmp=-1;
			FOR(cl,0,C)
				tmp=max(tmp,brd[rw][cl]);

			FOR(cl,0,C)
				rwMx[rw][cl]=tmp;
		}
		FOR(cl,0,C){
			int tmp=-1;
			FOR(rw,0,R)
				tmp=max(tmp,brd[rw][cl]);

			FOR(rw,0,R)
				clMx[rw][cl]=tmp;
		}

		bool posb=1;
		FOR(rw,0,R)		FOR(cl,0,C)
			posb&=(brd[rw][cl]==rwMx[rw][cl] || brd[rw][cl]==clMx[rw][cl]);

		(posb)?printf("YES\n"):printf("NO\n");
	}

	return 0;
}
