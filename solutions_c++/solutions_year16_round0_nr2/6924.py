 #include<iostream>
#include<cstdio>
#include<string>
using namespace std;
int main()
{
	long long t,i,j,k,temp,i1;
	string x,z;
	cin>>t;
	for(i1=1;i1<=t;i1++)
	{
		cin>>x;
		long long co=0;
		cout<<"Case "<<"#"<<i1<<": ";
		for(j=0;j<x.size();j++)
		{
			if(x[j]=='+')
				co++;
		}
		if(co==x.size())
		{
			cout<<0<<"\n";
		}
		else
		{
			long long co=0;
			while(1)
			{
				co=co+1;
				z="";
				
				for(i=x.size()-1;i>=0;i--)
				{
					if(x[i]=='-')
						break;
				}
				for(j=0;j<x.size();j++)
				{
					if(j<=i)
					{
						if(x[j]=='+')
							z=z+'-';
						else
							z=z+'+';
					}
				}
				temp=0;
				for(j=0;j<z.size();j++)
				{
					if(z[j]=='+')
						temp++;
				}
				if(z.size()==temp)
					break;
				x=z;

			}
			cout<<co<<"\n";
		}


	}
}