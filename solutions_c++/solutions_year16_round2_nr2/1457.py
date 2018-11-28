#include<iostream>
using namespace std;
int mtch(int x,string y)
{
	for(int i=y.length()-1;i>=0;i--)
	{
		if((y[i])<'0' || y[i]>'9')
		{
			x/=10;
			continue;
		}
		else if((y[i]-'0')!=x%10)
		{
		return 0;
		}
		x/=10;
		
	}
	if(x>0)
	return 0;
	return 1;
}
int abbs(int a,int b){if(a>b)
return a-b;
else
return b-a;
}
void disp(int x,string y)
{
	for(int i=y.length()-1;i>=0;i--)
	{
		if((y[i])<'0' || y[i]>'9')
		{
			y[i]=(x%10)+'0';
			x/=10;
		}
		else
		x/=10;
		
	}
	cout<<y;
}
int main()
{
	int test;
	cin>>test;
	for(int tt=1;tt<=test;tt++)
	{
		string a,b;
		cin>>a>>b;
		int ansa=0,ansb=1000000;
		for(int i=0;i<1001;i++)
		{
			for(int j=0;j<1001;j++)
			{
				if(mtch(i,a) && mtch(j,b))
				{
					if(abbs(i,j)<abbs(ansa,ansb))
					{
						ansa=i;ansb=j;
					}
					else if(abbs(i,j)==abbs(ansa,ansb))
					{
						if(i<ansa)
						{
							ansa=i;
							ansb=j;
						}
						else if(i==ansa && j<ansb)
						{
							ansa=i;
							ansb=j;
						}
					}
				}
			}
		}
		cout<<"Case #"<<tt<<": ";
		disp(ansa,a);
		cout<<" ";
		disp(ansb,b);
		cout<<endl;
	}
	return 0;
}
