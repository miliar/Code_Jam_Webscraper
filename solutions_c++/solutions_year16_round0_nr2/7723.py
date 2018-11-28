#include <bits/stdc++.h>
using namespace std;
void char_to_num(int a[],char s[],int n)
{
	int i;
	for(i=0;i<n;i++)
	{
		if(s[i]=='+')
			a[i]=1;
		else
			a[i]=0;
	}
}
int total(int a[],int n)
{
	int sum=0,i;
	for(i=0;i<n;i++)
		sum+=a[i];
	return sum;
}
void flip(int a[],int k,int n)
{
	int b[110],i;
	for(i=0;i<=k;i++)
		b[i]=!a[i];
	for(i=k;i>=0;i--)
		a[k-i]=b[i];
}
int main()
{
	FILE *in,*out;
	in=fopen("B-large.in","r");
	out=fopen("output.txt","w");
	int t,a[110],count,i,j,k,n;
	char s[110];
	fscanf(in,"%d",&t);
	for(i=1;i<=t;i++)
	{
		fscanf(in,"%s",s);
		fprintf(out,"Case #%d: ",i );
		n=strlen(s);
		count=0;
		char_to_num(a,s,n);
		while(total(a,n)!=n)
		{
			j=0;
			while(a[j]!=0)
				j++;
			k=j;
			while(k<n  && a[k]!=1)
				k++;
			if(j!=0)
			{
				flip(a,j-1,n);
				flip(a,k-1,n);
				count+=2;
			}
			else
			{
				flip(a,k-1,n);
				count+=1;
			}

		}
		fprintf(out,"%d\n",count );
	}
	return 0;
}