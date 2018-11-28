 #include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int taken[15];
int main()
{
	long long t,i,number,temp,total,x,y,p,q,co;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>number;
		memset(taken,0,sizeof(taken));
		cout<<"Case "<<"#"<<i<<": ";
		if(number==0)
		{
			cout<<"INSOMNIA\n";
			 continue;
		}
		else
		{
			temp=1,total=0;
			co=0;
			while(1)
			{
				total++;
				x=number*temp;
				temp++;
				y=x;
				while(y)
				{
					p=y%10;
					if(taken[p]==0)
					{
						co++;
						taken[p]=1;
					}
					y=y/10;

				}
				if(co==10)
					break;
			}
			cout<<x<<"\n";
		}
	}

}