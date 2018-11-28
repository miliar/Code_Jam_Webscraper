#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int t,h=1;
	FILE *fp1,*fp2;
    fp1=fopen("A-small-attempt2.in","r");
    fp2=fopen("output.txt","w");
    fscanf(fp1,"%d\n",&t);
	while(t--)
	{
		int x,a[4][4],b[16]={0},num1=0,num2=0,ans;
		bool flag=false;
		fscanf(fp1,"%d",&x);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				fscanf(fp1,"%d",&a[i][j]);
				if(x-1==i)
					b[a[i][j]-1]++;
			}
		fscanf(fp1,"%d",&x);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				fscanf(fp1,"%d",&a[i][j]);
				if(x-1==i)
					b[a[i][j]-1]++;
			}
		for(int i=0;i<16;i++)
			if(b[i]==1)
				num1++;
			else if(b[i]==2)
			{
				ans=i+1;
				num2++;
			}
		if(num1==8)
			fprintf(fp2,"Case #%d: Volunteer cheated!\n",h);
		else if(num2>=2)
			fprintf(fp2,"Case #%d: Bad magician!\n",h);
		else
			fprintf(fp2,"Case #%d: %d\n",h,ans);
		h++;
	}
	return 0;
}