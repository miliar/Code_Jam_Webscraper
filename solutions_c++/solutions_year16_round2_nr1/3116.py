#include <stdio.h>
#include <fstream>
#include <string.h>
using namespace std;

int main()
{
	long n;
	ifstream myfile;
	ofstream myfile1;
	myfile.open ("A-large.in");
	myfile>>n;
	myfile1.open("Output1");
	int i,j,k;
	for(i=0;i<n;i++)
	{
		char st[2005];
		int arra[10]={0};
		int z = 0,o=0,t=0,x=0,s=0,w=0,u=0,f=0,g=0,n=0,h=0,r=0;
		myfile>>st;
		for(j=0;j<strlen(st);j++)
		{
			if(st[j]=='Z')
			{
				z++;
			}
			if(st[j]=='W')
			{
				w++;
			}
			if(st[j]=='O')
			{
				o++;
			}
			if(st[j]=='X')
			{
				x++;
			}
			if(st[j]=='U')
			{
				u++;
			}
			if(st[j]=='F')
			{
				f++;
			}
			if(st[j]=='S')
			{
				s++;
			}
			if(st[j]=='G')
			{
				g++;
			}
			if(st[j]=='N')
			{
				n++;
			}
			if(st[j]=='T')
			{
				t++;
			}
			if(st[j]=='H')
			{
				h++;
			}
			if(st[j]=='R')
			{
				r++;
			}
		}
		arra[0]=z;
		arra[1]=(o-z-w-u);
		arra[2]=w;
		arra[3]=r-z-u;
		arra[4]=u;
		arra[5]=f-u;
		arra[6]=x;
		arra[7]=s-x;
		arra[8]=h-arra[3];
		arra[9]=(n-arra[7]-arra[1])/2;
		myfile1<<"Case #"<<(i+1)<<": ";
		for(j=0;j<10;j++)
		{
			while(arra[j]--)
			{
				myfile1<<j;
			}
		}
		myfile1<<endl;
	}
	myfile.close();
	myfile1.close();
}