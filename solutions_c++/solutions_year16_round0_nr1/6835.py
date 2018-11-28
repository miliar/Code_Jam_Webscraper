#include<iostream>
#include<math.h>

using namespace std;
int main()
{
	int t,p=1;;
cin>>t;
	while(t--)
	{	
		int i=0,flag=1;
		long long int hash[10]={0};
		long long int no,num,k,rem=0;
		cin>>no;
		cout<<"Case #"<<p<<": ";
		i=0;
		k=no;
		flag=1;
		
		if(no==0)
			{cout<<"INSOMNIA\n";}
		else
		while(flag==1)
		{	
				i++;
				no=k*(i);
				num=no;
			while(num)
			{
				rem=num%10;
				num=num/10;
				hash[rem]=1;
			}
			
			//cout<<no<<" ";
			
			for(int j=0;j<=9;j++)
			{
				if(hash[j]==0)
				{ flag=1;
					break;
				}
				else
					flag=0;
			}

		}
		if(k!=0)
		cout<<k*i<<"\n";

		p++;

	
	}	

	return	0;

}