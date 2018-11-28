#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <stdlib.h>
using namespace std;
int gys(int num1,int num2)//求两个数的最大公约数。
{
    int t,ys=1;//ys是余数，t是中间变量。
    int i=2;
    if(num1<num2)
    {
        t=num1;
        num1=num2;
        num2=t;
    }
    if(num1%num2==0)return num2;
    else
    {
        while(1)
        {
            if((num1%i==0) && (num2%i == 0))
            {
                ys*=i;
                num1=num1/i;
                num2=num2/i;
            }
            if(i==num2)
                return ys;
            i++;
        }
    }
}
int d2(int y)
{
	int t = 0;
	while (y!=1)
	{
		if (y % 2!=0)
			return 0;
		else
		{
			t ++;
			y /= 2;
		}
	}
	return t;
}
int main()
{
	freopen("A-small-attempt2.in","r",stdin);
	freopen("A-small-attempt2.out","w",stdout);
	
	int t;
	cin>>t;
	for (int tt=1;tt<=t;tt++)
	{
		cout<<"Case #"<<tt<<": ";
		int x,y;
		char ch;
		cin>>x>>ch>>y;
		int g = gys(x,y);
		x = x/g;
		y = y/g;
		if (x>y) 
			cout<<"impossible";
		else
		{
			if (d2(y)==0) cout<<"impossible";
			else
			{
				if (x>y/2) cout<<"1";
				else
				{
					int t=0;
					while (x<y/2)
					{
						x *=2;
						t++;
					}
					cout<<t+1;
				}
			}
		}
		cout<<"\n";
	}
	return 0;
}