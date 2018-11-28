#include<iostream>
#include<stdio.h>
using namespace std;
main()
{
	freopen("D-small.in", "r", stdin);
	freopen("out.txt", "w", stdout);
long long int t,b,z,x,r,c,y,u,i;
	cin>>t;
	z=0;
	while(z<t)
	{
		cin>>x>>r>>c;
		y=x;
		if((r*c)%x!=0)
		b=0;
		else if(x>c&&x>r)
		b=0;
		else
		{
			if((x>2) && (x%2==0) && (r==x/2 || c==x/2) && (x==r || x==c))
			{
				b=0;
			}
			else
			{
			  if(x%2==1)
			  x++;
			  x=x/2;
			  if(x>r||x>c)
			  {
			   b=0;
		      }
			  else
			  { 
			    b=1;
		      }
		    }
		}
	
		if(b==0)
		cout<<"Case #"<<z+1<<":"<<" "<<"RICHARD"<<"\n";
		else
		cout<<"Case #"<<z+1<<":"<<" "<<"GABRIEL"<<"\n";
		z++;
	}
}
