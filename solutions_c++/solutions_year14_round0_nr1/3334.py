#include<cstdio>
using namespace std;
int main()
{
	int t,h=1;
	FILE *fp1,*fp2;
    fp1=fopen("A-small-attempt0.in","r");
    fp2=fopen("output.txt","w");
    fscanf(fp1,"%d\n",&t);
	while(t--)
	{
		int x,mat[4][4],arr[16]={0},n1=0,n2=0,sol;
		bool flag=false;
		fscanf(fp1,"%d",&x);
		for(int i=0;i<4;i++)
			 for(int j=0;j<4;j++)
			{
				fscanf(fp1,"%d",&mat[i][j]);
				if(x-1==i)
					arr[mat[i][j]-1]++;
			}
		fscanf(fp1,"%d",&x);
		 for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				fscanf(fp1,"%d",&mat[i][j]);
				if(x-1==i)
					arr[mat[i][j]-1]++;
			 }
		for(int i=0;i<16;i++)
			if(arr[i]==1)
				n1++;
			else if(arr[i]==2)
			{
				sol=i+1;
				n2++;
			}
		if(n1==8)
		fprintf(fp2,"Case #%d: Volunteer cheated!\n",h);
		else if(n2>=2)
		fprintf(fp2,"Case #%d: Bad magician!\n",h);
		else
			fprintf(fp2,"Case #%d: %d\n",h,sol);
		h++;
	}
	return 0;
}