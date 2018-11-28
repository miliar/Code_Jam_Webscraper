#include<bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin>>t;
	int j=1;
	while(t--)
	{
		int n;
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<j<<":"<<" INSOMNIA"<<endl;
			
		}
		else
		{	
		
			long long int num=0,res=0;
			int x;
		
			int count[10]={0};
			int i=1;
			while(1)
			{
				num=n*i;
				res=num;
			
				i++;
				while(num)
				{
					x=num%10;
					count[x]++;
					num=num/10;
				}
			
				if(count[0]>0&&count[1]>0&&count[2]>0&&count[3]>0&&count[4]>0&&count[5]>0&&count[6]>0&&count[7]>0&&count[8]>0&&count[9]>0)
				{
					cout<<"Case #"<<j<<": "<<res<<endl;
					break;
				}
			
			
			
			}
			
		}
		j++;
	}
	
	return 0;
}
