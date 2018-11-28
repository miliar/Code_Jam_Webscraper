#include<bits/stdc++.h>
using namespace std;

int a[10], num;

int check()
{
	int flag = 1;
	for(int i=0; i<10; i++)
		if(a[i]!=1)
		{
			flag = 0;
			break;
		}
	return flag;
}

int main()
{
	int n;
	cin>>n;
	for(int z=0; z<n; z++)
	{
		scanf("%d", &num);
		int numB=num, chk=0, x=2, numC=0;
		if(num==0)
		{
			cout<<"Case #"<<(z+1)<<": INSOMNIA"<<endl;
			continue;
		}
		else
		{
			while(x<1000)
			{
				numC=num;
				while(num>0)
				{
					a[num%10]=1;
					num/=10;
				}
				if((chk=check())==1)
					break;
				else
				{
					num = numB*x;
					x++;
				}
			}
		}
		if(chk==1)
			cout<<"Case #"<<(z+1)<<": "<<numC<<endl;
		else
			cout<<"Case #"<<(z+1)<<": INSOMNIA"<<endl;
		for(int i=0; i<10; i++)
			a[i]=0;
	}
	
	return 0;
}














