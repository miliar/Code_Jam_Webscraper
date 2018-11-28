#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cstring>

using namespace std;

char St[2001];
int E,F,G,H,I,N,O,R,S,T,U,V,W,X,Z;
int num[10];

int main(){
	int time;
	scanf("%d",&time);
	for(int t = 1;t<=time;t++){
		fill(St,St+2001,'\0');
		fill(num,num+10,0);
		scanf("%s",St);
		int n=strlen(St);
		sort(St,St+n);
		int i=0;
		for(E=0;St[i]=='E';E++,i++);
		for(F=0;St[i]=='F';F++,i++);
		for(G=0;St[i]=='G';G++,i++);
		for(H=0;St[i]=='H';H++,i++);
		for(I=0;St[i]=='I';I++,i++);
		for(N=0;St[i]=='N';N++,i++);
		for(O=0;St[i]=='O';O++,i++);
		for(R=0;St[i]=='R';R++,i++);
		for(S=0;St[i]=='S';S++,i++);
		for(T=0;St[i]=='T';T++,i++);
		for(U=0;St[i]=='U';U++,i++);
		for(V=0;St[i]=='V';V++,i++);
		for(W=0;St[i]=='W';W++,i++);
		for(X=0;St[i]=='X';X++,i++);
		for(Z=0;St[i]=='Z';Z++,i++);
		num[0]=Z;
		num[2]=W;
		num[4]=U;
		num[6]=X;
		num[8]=G;
		E-=Z;R-=Z;O-=Z;
		T-=W;O-=W;
		F-=U;O-=U;R-=U;
		S-=X;I-=X;
		E-=G;I-=G;H-=G;T-=G;
		num[3]=H;
		T-=H;R-=H;E-=H;E-=H;
		num[5]=F;
		I-=F;V-=F;E-=F;
		num[9]=I;
		N-=I;N-=I;E-=I;
		num[1]=O;
		N-=O;E-=O;
		num[7]=S;
		printf("Case #%d: ", t);
		for (int i = 0; i < 10; i++) {
			for(int j = 0;j < num[i]; j++){
				printf("%d",i);
			}
		}
		printf("\n");
	}
	return 0;
}
