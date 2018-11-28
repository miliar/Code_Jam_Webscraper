#include<iostream>
#include<cmath>
using namespace std;
int check_pal(int a)
{
	int x=a, d,rev=0;
	while(x>0)
	{
		d=x%10;
		rev=rev*10+d;
		x=x/10;
		}
	if(a==rev)
	return 1;
	else 
	return 0;
}

int main()
{int i,t,j,n,y,c;

cin>>t;
int a[t][2];
//n=t;	
		
			for(i=0;i<t;i++)
			{
				for(j=0;j<2;j++)
					cin>>a[i][j];
			}

	    
	for(i=0;i<t;i++)
	{	c=0;
		for(j=a[i][0];j<=a[i][1];j++)
		{	y=sqrt(j);
			
			if((check_pal(j)==1)&&(y*y==j)&&(check_pal(y)==1))
					
						c++;
		}
	cout<<"Case #"<<(i+1)<<": "<<c<<"\n";
	}
return 0;
}
