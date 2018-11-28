#include <bits/stdc++.h>
#define maxn 10

using namespace std;

int ar[maxn][maxn],er[maxn][maxn];

int main(){
	int N,a1,a2,cnt=0,tut;
	scanf(" %d",&N);
	for(int i=1;i<=N;i++){
		cnt=0;
		scanf(" %d",&a1);
		for(int j=1;j<=4;j++)
			for(int k=1;k<=4;k++)
				scanf(" %d",&ar[j][k]);
		scanf(" %d",&a2);
		for(int j=1;j<=4;j++)
			for(int k=1;k<=4;k++)
				scanf(" %d",&er[j][k]);
		for(int j=1;j<=4;j++)
			for(int k=1;k<=4;k++)
				if(ar[a1][j]==er[a2][k]){
					er[a2][k]=-1;
					cnt++;
					tut=ar[a1][j];
				}
		if(cnt==1)
			printf("Case #%d: %d\n",i,tut);
		else if(!cnt)
			printf("Case #%d: Volunteer cheated!\n",i);
		else
			printf("Case #%d: Bad magician!\n",i);
	}
	return 0;
}
