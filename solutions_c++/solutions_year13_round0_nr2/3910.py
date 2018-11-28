#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
using namespace std;


int main()
{
	int T=0;
	int i,j,k;
	int N,M;
	int flag;
	int a[110][110];
	int rhest[110],chest[110];
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	cin>>T;
	for(i=1;i<=T;i++) {
		cin>>N>>M;
		flag=1;
		memset(a,0,sizeof(a));
		memset(rhest,0,sizeof(rhest));
		memset(chest,0,sizeof(chest));
		for(j=0;j<N;j++)
			for(k=0;k<M;k++) {
				cin>>a[j][k];
				if (a[j][k]>rhest[j]) {
					rhest[j]=a[j][k];
				}
				if (a[j][k]>chest[k]) {
					chest[k]=a[j][k];
				}
			}
		for(j=0;j<N;j++) {
			for(k=0;k<M;k++) {
				if (a[j][k]>=rhest[j] || a[j][k]>=chest[k]) {
					flag=1;
				}
				else flag=0;
				if (flag==0) break;
			}
			if (flag==0) break;
		}
		if (flag==1) printf("Case #%d: YES\n",i);
		else printf("Case #%d: NO\n",i);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
