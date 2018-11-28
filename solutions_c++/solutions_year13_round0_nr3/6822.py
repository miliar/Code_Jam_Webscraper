#include<iostream>
using namespace std;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	long long n,x,y,b,count=0,w=0,g,v=0;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		cin>>x>>y;
		for(int l=x;l<=y;l++)
		{
			if(l<=9)
			{
				int  h=sqrt(l);
				if(h*h==l)
					count++;
			}
			else
			{
				 b=l;
				while(b>0)
				{
					 g=b%10;
					 v=v*10+g;
					 b/=10;
				}
			
				if(v==l)
				{
					int h=sqrt(l);
					if(h<=9)
					{
						if(h*h==l)
						 count++;
					}
					else
					{
						b=h;
						while(b>0)
						{
							g=b%10;
							w=w*10+g;
							b/=10;
						}
						if(w==h)
						{
							if(h*h==l)
								count++;
						}
					}
				}	
			}		
			v=0;
			w=0;
		}
		cout<<"Case #"<<i+1<<": "<<count<<endl;
		count =0;
	}
}