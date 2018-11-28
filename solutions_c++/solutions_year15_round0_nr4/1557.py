#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>
#include<math.h>
using namespace std;
string halamad(int r,int c,int x);
int main()
{
	int z;
    int x,r,c;
	cin>>z;
	int m=1;
	while(z--)
	{
	
		cin>>x>>r>>c;
		cout<<"Case #"<<m<<": "<<halamad(r,c,x)<<"\n";
		m++;
	}
	return 0;
}
string halamad(int r,int c,int x)


{
	       if((r*c)%x!=0)
		{
			return "RICHARD";
		}	
		else 
		{
			if(x<=2)
			{
				return "GABRIEL";
			}
			else if(x==3)
			{
				if((r*c)==3)
				{
					return "RICHARD";
				}
				else
				{
				return "GABRIEL";
				}
			}
			else if((r*c)==4 || (r*c)==8)
			{
			return "RICHARD";
			}
			else if((r*c)==12 || (r*c)==16)
			{
			  return "GABRIEL";
			}
		}
}