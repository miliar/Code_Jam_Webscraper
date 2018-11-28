#include<iostream>
#include<math.h>
using namespace std;
int ispal(double n)
{
	int p=(int)n,r,s=0;
	while(p>0)
	{
		r=p%10;
		s=s*10+r;
		p=p/10;
	}
	if(s==n)
		return 1;
	else
		return 0;
}

int main()
{
	int ch,n,t=1,c=0,x,y;	
	double p;
	freopen("C-small-attempt1.in","rt",stdin);
	freopen("C.out","wt",stdout);
	cin>>ch;
	while(ch>0)
	{
		c=0;
		cin>>x;cin>>y;
		for(int i=x;i<=y;i++)
		{
			if(ispal(i))
			{
				p=sqrt(i);
				if(ispal(p))
				{
					c++;
				}
			}
		}
		cout<<"Case #"<<t<<": "<<c<<"\n";
		ch--;t++;
	}
	
						
	return 0;
}
