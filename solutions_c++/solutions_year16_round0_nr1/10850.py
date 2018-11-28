#include<iostream>
#include<fstream>
using namespace std;
void splitdigits(int n,int *a);
int main()
{
	int t,n,a[10],c,flag;
	fstream infile("A-large (1).in");
	fstream outfile("samplesheepoutput.txt");
	infile>>t;
	for(int z=0;z<t;z++)
	{
		for(c=0;c<10;c++)
		{
			a[c]=0;
		}
		infile>>n;
		int j=1;
		while(j!=1000)
		{
			int k;
			k=n*j;
			splitdigits(k, a);
			
			flag=0;
			for(int i=0;i<10;i++)
			{
				
				if(a[i]==1)
				{

					flag++;
				}
		    }
		    if(flag==10)
		    {
		    	outfile<<"Case #"<<z+1<<": "<<k<<endl;
		    	break;
		    }
		    else
		    	j++;
		}
		if(flag!=10)
		{
			outfile<<"Case #"<<z+1<<": INSOMNIA"<<endl;
		}
	}
}
void splitdigits(int n,int *a)
{
	int d;
	while(n!=0)
	{
		d=n%10;
		a[d]=1;
		n=n/10;
	}
}
