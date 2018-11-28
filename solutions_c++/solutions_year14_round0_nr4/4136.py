#include <bits/stdc++.h>
#include <stdio.h>
using namespace std;
int main()
{
	int t,cnt=0,i,j;
	FILE *fp,*fp1;
	fp=fopen("fin.in","r");
	fp1=fopen("fout.out","w");
	fscanf(fp,"%d",&t);
	while(t--)
	{
		cnt++;
		int n,dw,w;
		fscanf(fp,"%d",&n);
		float a[n],b[n];
		for(i=0;i<n;i++)
		{
			fscanf(fp,"%f",&a[i]);
		} 
		for(i=0;i<n;i++)
		{
			fscanf(fp,"%f",&b[i]);
		}
		sort(a,a+n);
		sort(b,b+n);
		i=0;j=0;
		if(n==1)
		{
			if(a[0]>b[0])
			{
				w=1;
				dw=1;
			}
			else
			{
				w=0;
				dw=0;
			}
			fprintf(fp1,"Case #%d: %d %d\n",cnt,dw,w);
		}
		else
		{
		while(j!=n)
		{
			if(b[j]<a[i])
			{
				j++;
			}
			else
			{
				i++;
				j++;
			}
		}
		w=n-i;
		i=0;j=0;
		while(i!=n)
		{
			if(a[i]<b[j])
			{
				i++;
			}
			else
			{
				i++;
				j++;
			}
		}
		dw=j;
		fprintf(fp1,"Case #%d: %d %d\n",cnt,dw,w);
		}
	}
	fclose(fp);
	fclose(fp1);
	return 0;
}