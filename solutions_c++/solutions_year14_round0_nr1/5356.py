#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int a[10][10],b[10][10];
int bo[100];

int check(int n,int m){
	int k=-100000;
	memset(bo,0,sizeof(bo));
	for (int i=1; i<=4; ++i)
		for (int j=1; j<=4; ++j)
			if (a[n][i]==b[m][j]){
				if (k==-100000 || k==a[n][i]){
					k=a[n][i];
					continue;
				}
				return -1;
			}
	if (k==-100000) return -2;
	return k;
}

int main(){
	//freopen("1.txt","r",stdin);
	//freopen("1.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int I=1; I<=T;++I){
		int n,m;
		scanf("%d",&n);
		for (int i=1; i<=4; ++i)
			for (int j=1; j<=4; ++j)
				scanf("%d",&a[i][j]);
		scanf("%d",&m);
		for (int i=1; i<=4; ++i)
			for (int j=1; j<=4; ++j)
				scanf("%d",&b[i][j]);
		int z1=check(n,m);
		printf("Case #%d: ",I);
		if (z1==-2) puts("Volunteer cheated!");
		else if (z1==-1) puts("Bad magician!");
		else printf("%d\n",z1);
	}
}
