#include <iostream>
#include <cstdio>
using namespace std;

int N,S,R,P,T,xx,yy,zz,x,y,z;
int f1[111],f2[111],f3[111];
int g1[111],g2[111],g3[111];

int result(char c,int x){
	if (x==0) {
		printf("%c",c);
		return 0;
	}
	if (c == 'R'){
		if (g1[x-1] > g2[x-1]){
			result('R',x-1);
			result('S',x-1);
		} else {
			result('S',x-1);
			result('R',x-1);
		}
		return 0;
	}
	if (c == 'S'){
		if (g3[x-1] > g2[x-1]){
			result('P',x-1);
			result('S',x-1);
		}else {
			result('S',x-1);
			result('P',x-1);
		}
		return 0;
	}
	if (c == 'P'){
		if (g3[x-1] > g1[x-1]){
			result('P',x-1);
			result('R',x-1);
		} else {
			result('R',x-1);
			result('P',x-1);
		}
		return 0;
	}
}

int func(int x,int y){
	if (x > y) return x*10+y;else return y*10+x; 
}
int rankd(int num){
	int x=xx,y=yy,z=zz,t;
	if (z>y){
		t = y;
		y = z;
		z = t;
	}
	if (y>x){
		t = x;
		x = y;
		y = t;
	}
	if (z>y){
		t = y;
		y = z;
		z = t;
	}
	//printf("%d  %d  %d\n",x,y,z );
	if (num == x) return 2;
	if (num == y) return 1;
	if (num == z) return 0;
}
int main(int argc, char const *argv[]){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);


	f1[0]=1;f2[0]=0;f3[0]=0;
	for (int i = 1; i < 13; ++i){
		f1[i]=f1[i-1]+f3[i-1];
		f2[i]=f2[i-1]+f1[i-1];
		f3[i]=f3[i-1]+f2[i-1];
	}
	//RSP
	g1[0]=1;g2[0]=0;g3[0]=2;
	for (int i = 1; i < 13; ++i){
		x = g1[i-1]; y= g2[i-1]; z= g3[i-1];
		xx = func(x,y); yy = func(y,z); zz =func(z,x);
		//if (i==1) printf("R:%d  S:%d  P:%d\n",xx,yy,zz );
		g1[i] = rankd(xx); g2[i] = rankd(yy); g3[i]=rankd(zz);
	}
	//printf("R:%d  S:%d  P:%d\n",g1[1],g2[1],g3[1] );
	cin>>T;
	for (int i = 1; i <= T; ++i){
		printf("Case #%d: ", i);
		cin>>N>>R>>P>>S;//RSP
		//cout <<N << R <<P <<S<<endl;
		//if (g3[N]==2&&g1[N]==1&&g2[N]==0){
			//P
			if (P==f1[N]&&R==f2[N]&&S==f3[N]) {
				result('P',N);
				printf("\n");
				continue;
			}
			//R
			if (R==f1[N]&&S==f2[N]&&P==f3[N])  {
				result('R',N);
				printf("\n");
				continue;
			}
			//S
			if (S==f1[N]&&P==f2[N]&&R==f3[N])  {
				result('S',N);
				printf("\n");
				continue;
			}
		// } else 
		// if (g3[N]==2&&g2[N]==1&&g1[N]==0){
		// 	//P
		// 	if (P==f1[N]&&R==f2[N]&&S==f3[N]) {
		// 		result('P',N);
		// 		printf("\n");
		// 		continue;
		// 	}
		// 	//S
		// 	if (S==f1[N]&&P==f2[N]&&R==f3[N])  {
		// 		result('S',N);
		// 		printf("\n");
		// 		continue;
		// 	}
		// 	//R
		// 	if (R==f1[N]&&S==f2[N]&&P==f3[N])  {
		// 		result('R',N);
		// 		printf("\n");
		// 		continue;
		// 	}
		// } else 
		// if (g3[N]==1&&g2[N]==0&&g1[N]==2){
		// 	//P
		// 	if (P==f1[N]&&R==f2[N]&&S==f3[N]) {
		// 		result('P',N);
		// 		printf("\n");
		// 		continue;
		// 	}
		// 	//S
		// 	if (S==f1[N]&&P==f2[N]&&R==f3[N])  {
		// 		result('S',N);
		// 		printf("\n");
		// 		continue;
		// 	}
		// 	//R
		// 	if (R==f1[N]&&S==f2[N]&&P==f3[N])  {
		// 		result('R',N);
		// 		printf("\n");
		// 		continue;
		// 	}
		// }
		printf("IMPOSSIBLE\n");


	}
	return 0;
}