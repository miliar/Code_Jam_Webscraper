#include<iostream>
#include<conio.h>

using namespace std;

void main()
{
	int a,b,reverse,rem;
	int n,temp,count;
	int reverse1,temp1,rem1;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		count=0;
		cin>>a>>b;
		for(int j=a;j<=b;j++)
		{
			int p=j;
			reverse=0;
			while(p!=0)
			{
				rem=p%10;
				reverse=reverse*10+rem;
				p/=10;
			}  
			if (reverse==j)
			{
				for(int s=1;s<=j/2 || s==j/2+1;s++)
				{
					int s1=s;
					if(reverse==s*s)
					{
						reverse1=0;
						while(s1!=0)
						{
							rem1=s1%10;
							reverse1=reverse1*10+rem1;
							s1/=10;
						}  
						if(reverse1==s)
						{
							count++;
						}
					}
				}
			}
		}
		cout<<"Case #"<<i+1<<": "<<count<<"\n";
	}
	getch();
}