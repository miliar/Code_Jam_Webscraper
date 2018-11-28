#include<iostream>
#include<cmath>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cstdlib>
using namespace std;

typedef unsigned long long ull;

#define mod 1000000007
#define findmax(a,b) (a)>(b)?a:b
#define findmin(a,b) (a)<(b)?a:b

int maxstatus(double *a,double *b,int af,int al,int bf,int bl)
{	int naomi=0;
	while(af<=al)
	{
		if(a[af]<b[bf])
		{
			af++;bl--;
		}
		else 
		{
			bf++;af++;naomi++;
		}
	}
	
return naomi;	
	
}

int status(double *a,double *b,int af,int al,int bf,int bl)
{
	int naomi=0;
	while(al>=af)
	{
		if(a[al]>b[bl])
		{
			al--;bf++; naomi++;
		}
		else 
		{
			al--;bl--;
		}
	}	
return naomi;
}



int main()
{
	int t;
	
	FILE *in,*out;
	in=fopen("D-large.in","r");
	out=fopen("Dsmall.out","w");
	fscanf(in,"%d",&t);
	for(int z=1;z<=t;z++)
	{
		int n,i;
		fscanf(in,"%d",&n);
		
		double a[n],b[n];
		for(i=0;i<n;i++)
		fscanf(in,"%lf",&a[i]);
		for(i=0;i<n;i++)
		fscanf(in,"%lf",&b[i]);
		/*	
		cout<<"A"<<endl;
		for(i=0;i<n;i++)
		cout<<a[i]<<" ";
		cout<<endl;
		
		cout<<"B"<<endl;
		for(i=0;i<n;i++)
		cout<<b[i]<<" ";
			cout<<endl;
			*/
		sort(a,a+n); sort(b,b+n);
	//	int af=0,al=n-1,bf=0,bl=n-1,ans,maxans=-1;
	
		/*while(n>0)
		{
			ans=status(a,b,af,al,bf,bl);
			
			if(maxans<=ans)
				maxans=ans;
			if(ans==n)
				break;
			
			af++;
			bl--;
			n--;
		}		
		*/
		//cout<<status(a,b,af,al,bf,bl)<<endl;
		
	fprintf(out,"Case #%d: %d %d\n",z,maxstatus(a,b,0,n-1,0,n-1),status(a,b,0,n-1,0,n-1));	
	}//end of while
	
	return 0;
}