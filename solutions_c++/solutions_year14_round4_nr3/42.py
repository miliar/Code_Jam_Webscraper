#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> PI;
typedef long long LL;
typedef double D;
#define FI first
#define SE second
#define MP make_pair
#define PB push_back
#define R(I,N) for(int I=0;I<N;I++)
#define F(I,A,B) for(int I=A;I<B;I++)
#define FD(I,N) for(int I=N-1;I>=0;I--)
#define make(A) scanf("%d",&A)
int w,h,b;
int xx[] = {0,1,0,-1};
int yy[] = {1,0,-1,0};
#define MAX 1000
bool p[MAX][MAX];
bool dfs(int x,int y,int kier){
	if(x == -1 || x==w || y == -1 || p[x][y])return 0;
	p[x][y] = 1;
	if(y == h-1)return 1;
	R(i,4){
		int g = (i+kier)%4;
		if(dfs(x+xx[g],y+yy[g],(g+3)%4))return 1;
	}
	return 0;
}

void test(){
	static int test_nr = 0;test_nr++;
	printf("Case #%d: ",test_nr);
	make(w);make(h);make(b);
	R(i,w)R(j,h)p[i][j] = 0;
	R(i,b){
		int x1,y1,x2,y2;
		scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
		F(i,x1,x2+1)F(j,y1,y2+1){
			p[i][j] = 1;
		}
	}
	/*R(i,w){
		R(j,h)printf("%d",p[i][j]);
		puts("");
	}
		puts("");*/
	int wyn = 0;
	R(i,w){
		if(dfs(i,0,0))wyn++;
		/*R(i,w){
			R(j,h)printf("%d",p[i][j]);
			puts("");
		}
			puts("");
		*/
	}
	printf("%d\n",wyn);
}
main(){
	int _;make(_);while(_--)test();
}
