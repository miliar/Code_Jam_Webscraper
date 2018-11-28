                    //OM RAM JI
#include<stdio.h>
#include<string.h>
#include<fstream>
#include<iostream>
#include<algorithm>
#include<math.h>

using namespace std;
int f(int s,int k);
int b[100000],a,step,n,c;
int main()
{
	int tc,j,i,ste,stet;
	ifstream ifile("d:/a.txt");
	ofstream ofile("d:/a1.txt");
	ifile>>tc;
	
	for (j=0;j<tc;j++)
	{
		
		c=0;
		ste=0;
		ifile>>a>>n;
		step=n+1;
		for (i=0;i<n;i++)
		{
			ifile>>b[i];
		}
		sort(b,b+n);
		
		while (c!=n)
		{
			while (c<n&&a>b[c])
			{
				a=a+b[c];
				c++;
			}
			//printf("hi %d ",j);
			if (c<n&&a!=1)
			{
				
				//stet=ste;
			//	printf("going : %d %d %d",a,c,ste);
				ste=ste+f(0,ste);
			//	printf("hireturned  %d",ste);
				
			}
			else if (a==1)
			{
				ste=ste+n-c;
				c=n;
			}
			
		}
		if (ste<step)
		{
			step=ste;
		}	
		//ste=stet;
		//printf("%d",ste);
		ofile<<"Case #"<<j+1<<": "<<step<<endl;
	}
	return 0;
}

int f(int s,int k)
{
//	printf("\n ENTERED %d %d %d ",a,c,s);
	a=2*a-1;
	s++;
	int st=0;
	if (c<n&&a>b[c])
		return s;
	else
	{
		
		st=s+k+n-c-1;
		
		if (st<step)
		{//printf("\n break %d %d %d ",s,st,c);
			//printf("%d",st);
			step=st;
		}
		//printf("hisd");
		st=f(s,k);
		//printf("sd %d ",st);
		if (st<step)
		return st;
		

	}
}
