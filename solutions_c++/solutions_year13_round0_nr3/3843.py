#include<iostream>
#include<conio.h>
#include<math.h>
using namespace std;
bool checkpal(int n);
void main()
{
	int T;
	int A,B;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		cin>>A>>B;
		int y=0;
		for(int j=A;j<=B;j++)
		{
			if(checkpal(j))
			{
				int s=sqrt(j);
				if((s*s==j) && checkpal(sqrt(j)))
					y++;
			}
		}
		cout<<"Case #"<<i<<": "<<y<<endl;
	}
}
bool checkpal(int n)
{
	int sum=0;
	int m=n;
	int d=0;
	while(n!=0)
	{
		d=n%10;
		sum=10*sum+d;
		n=n/10;
	}
	if(m==sum)
		return true;
	else
		return false;
}