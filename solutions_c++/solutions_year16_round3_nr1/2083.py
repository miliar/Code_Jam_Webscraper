#include <bits/stdc++.h>
using namespace std;

int sum(int a[],int n)
{
	int i,sum=0;
	for(i=0;i<n;i++)
		sum+=a[i];
	return sum;
}
int max1(int a[],int n,int *pos)
{
	int i,max1=-1;
	for(i=0;i<n;i++)
	{
		if(a[i]>max1)
		{
			max1=a[i];
			*pos=i;
		}
	}

	return max1;
}
int max2(int a[],int n,int maxi,int pos)
{
	int i,count,pos2=-1 ;
	for(i=0;i<n;i++)
	{
		if(i!=pos && a[i]==maxi)
			pos2=i;
	}
	return pos2;
}
int main()
{
	FILE *in,*out;
	in=fopen("A.in","r");
	out=fopen("output.txt","w");
	int t,i,j,k,n,a[26],pos,pos2,maxi,maxi2;
	fscanf(in,"%d",&t);
	for(i=1;i<=t;i++)
	{
		fscanf(in,"%d",&n);
		for(j=0;j<n;j++)
			fscanf(in,"%d",&a[j]);
		fprintf(out,"Case #%d: ",i );
		while(sum(a,n)>0)
		{
			maxi=max1(a,n,&pos);
			maxi2=max2(a,n,maxi,pos);
			if(maxi2==-1)
			{
				if(a[pos]>=2)
				{
					a[pos]-=2;
					fprintf(out,"%c%c ",pos+65,pos+65 );
				}
				else
				{
					a[pos]-=1;
					fprintf(out,"%c ",pos+65 );
				}
			}
			else
			{
				if(a[pos]>=2 || sum(a,n)==2)
				{
					a[pos]-=1;
					a[maxi2]-=1;
					fprintf(out,"%c%c ",pos+65,maxi2+65);
				}
				else
				{
					a[pos]-=1;
					fprintf(out,"%c ",pos+65 );
				}

			}

		}

		fprintf(out,"\n");


	}
	fclose(in);
	fclose(out);
	return 0;
}