#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int mat[5][5],a[5],b[5];
int main(void)
{
	//freopen("C:\\Users\\ytimex\\Desktop\\gcj\\A-small-attempt0.in","rb",stdin);
	//freopen("C:\\Users\\ytimex\\Desktop\\gcj\\A-small-attempt0.out","wb",stdout);
	FILE *fin,*fout;
	fin  = fopen("C:\\Users\\ytimex\\Desktop\\gcj\\A-small-attempt7.in","rb");
	fout = fopen("C:\\Users\\ytimex\\Desktop\\gcj\\A-small-attempt0.out","wb");
	int T,n;
	fscanf(fin,"%d",&T);
	int t=1;
	while(t<=T)
	{
		memset(mat,0,sizeof(mat));
		fscanf(fin,"%d",&n);
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
				fscanf(fin,"%d",&mat[i][j]);
		for(int i=1;i<=4;i++)
			a[i-1] = mat[n][i];
		memset(mat,0,sizeof(mat));
		fscanf(fin,"%d",&n);
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
				fscanf(fin,"%d",&mat[i][j]);
		for(int i=1;i<=4;i++)
			b[i-1] = mat[n][i];
		sort(a,a+4);
		sort(b,b+4);
		int ans=0,num;
		int i=0,j=0;
		while(i<4 && j<4)
		{
			if(a[i]==b[j]) {num=a[i];ans++;i++;j++;}
			else if(a[i]>b[j]) {j++;}
			else i++;
		}
		if(ans==0) fprintf(fout,"Case #%d: Volunteer cheated!\n",t);
		else if(ans==1) fprintf(fout,"Case #%d: %d\n",t,num);
		else fprintf(fout,"Case #%d: Bad magician!\n",t);
		t++;
	}
	return 0;
}
