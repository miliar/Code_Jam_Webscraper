#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
	int t,i;
	ifstream in("input.txt");
	ofstream out("output.txt");
	in>>t;
	for(i=1;i<=t;i++)
	{
		int n;
		in>>n;
		int a[n],j,k=1;
		for(j=0;j<n;j++)
		in>>a[j];
		out<<"Case #"<<i<<": ";
		while(k)
		{
			int max=0,min=1001,v1,v2;
			for(j=0;j<n;j++)
			{
				if(max<a[j])
				{
					max=a[j];
					v1=j;
				}
				if(min>a[j]&&v1!=j)
				{
					min=a[j];
					v2=j;
				}
			}
			if(max>0&&min>0)
			{
				char aa,b;
				aa=(char)(v1+65);
					b=(char)(v2+65);
					
				if(max==min&&max!=1)
				{
					a[v1]-=1;
					a[v2]-=1;
					out<<aa<<b<<" ";
				}
				else if(max==1)
				{
					int o=0;
					for(j=0;j<n;j++)
					{
						if(a[j]==1)
						o++;
					}
					if(o%2==0)
					{
						a[v1]-=1;
					a[v2]-=1;
					out<<aa<<b<<" ";
					}
					else
					{
						a[v1]-=1;
						out<<aa<<" ";
					}
				}
				if(max!=min)
				{
					a[v1]-=1;
					out<<aa<<" ";
				}
				
			}
			else
			k=0;
			if(!k)
			out<<endl;
			
		}
	}
	
			
	
	return 0;
}
