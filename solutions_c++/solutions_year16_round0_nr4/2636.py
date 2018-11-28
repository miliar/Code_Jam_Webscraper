#include <bits/stdc++.h>
using namespace std;

bool check[101];

int main()
{
	FILE *fin,*fout;
	fin=fopen("D-small-attempt1.in","r");
	fout=fopen("D-small-attempt1.out","w");

	int t;
	// scanf("%d",&t);
	fscanf(fin,"%d",&t);
	for(int i=1;i<=t;i++)
	{
		int K,C,S;
		scanf("%d%d%d",&K,&C,&S);
		fscanf(fin,"%d%d%d",&K,&C,&S);
		// printf("Case #%d: ",i);
		fprintf(fout,"Case #%d: ",i);

		// for(int j=1;j<=K;j++) printf("%d ",j);
		// printf("\n");
		for(int j=1;j<=K;j++) fprintf(fout,"%d ",j);
		fprintf(fout,"\n");
	}
}

