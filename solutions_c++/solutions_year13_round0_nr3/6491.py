#include<iostream>
#include<math.h>
using namespace std;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int x,y,l,n=0,r,palin=0,c=0,t;
	cin>>t;
	int k=0;
	while(k<t)
	{
		cin>>x>>y;
		l=x;
		for(int i=l;i<=y;i++)
		{
			r=i;
			while(r!=0)
			{
				n=r%10;
				c+=n;
				c*=10;
				r/=10;

			}
			c/=10;
			if(c==l)
			{
			 	c=0;
			    n=0;
				int y=sqrt(l);
				r=y;
				if(y*y == l)
				{
					while(r!=0)
					{
						n=r%10;
						c+=n;
						c*=10;
						r/=10;

					}
					c/=10;
					if(c==y)
					{
						palin++;
					}
				}
			}
			c=0;
			n=0;
			l++;
		}
		cout<<"Case #"<<k+1<<": "<<palin<<endl;
		palin=0;
		k++;
	}
	return 0;
}
