#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
int main()  
{
	FILE *fin,*fout;
	fin=fopen("A-small-attempt0.in","rb");
	fout=fopen("A-small-attempt0.out","wb");
	int r,i,j,n,t,row,count,index;
	bool s1[17];
	bool s2[17];
	fscanf(fin,"%d",&t);
	for(r=1;r<=t;r++)
	{
		fscanf(fin,"%d",&row);
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
			{
				fscanf(fin,"%d",&n);
				if(i==row)
					s1[n]=true;
				else
					s1[n]=false;
			}
		fscanf(fin,"%d",&row);
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
			{
				fscanf(fin,"%d",&n);
				if(i==row)
					s2[n]=true;
				else
					s2[n]=false;
			}
		count=0;
		for(i=1;i<=16;i++)
		{
			s1[i]=s1[i]&&s2[i];
			if(s1[i])
			{
				index=i;
				count++;
			}
		}
		if(count==0)
			fprintf(fout,"Case #%d: Volunteer cheated!\n",r);
		else if(count==1)
			fprintf(fout,"Case #%d: %d\n",r,index);
		else
			fprintf(fout,"Case #%d: Bad magician!\n",r);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}