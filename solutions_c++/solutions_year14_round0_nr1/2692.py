#include <bits/stdc++.h>
const int N=4;
int A[N][N],B[N][N];
int a,b;
void read(int &a,int A[][N]){
	scanf("%d",&a);a--;
	for(int i=0;i<N;i++)
		for(int j=0;j<N;j++)
			scanf("%d",&A[i][j]);
}
int main(){
	int w=1;
	int T;scanf("%d",&T);
	while(T--){
		read(a,A);
		read(b,B);
		int cnt=0,ans=-1;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(A[a][i]==B[b][j]){
					cnt++;
					ans=A[a][i];
				}
		printf("Case #%d: ",w++);
		if(cnt==1)printf("%d\n",ans);
		else if(cnt>1)printf("Bad magician!\n");
		else printf("Volunteer cheated!\n");
	}
}
