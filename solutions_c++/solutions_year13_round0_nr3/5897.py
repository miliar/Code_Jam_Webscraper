#include<iostream>
#include<math.h>
using namespace std;
int ispal(int n)
{
	int dig[5];
	int pos=0;
	while(n!=0)
	{
		dig[pos++]=n%10;
		n/=10;
	}
	int i,j;
	for(i=0,j=pos-1;i<j;i++,j--)
		if(dig[i]!=dig[j])
			return 0;
			
	return 1;
}
int main()
{
	int t;
	cin>>t;
	int copy=t;
	while(t--)
	{
		int a,b;
		cin>>a>>b;
		int count=0;
		int temp=(int)sqrt(a);
		int start;
		if(temp*temp==a)
			start=temp;
		else
			start=temp+1;
		for(int i=start;i<=sqrt(b);i++)
		{
			if(ispal(i)&&ispal(i*i))
				{
					//cout<<i<<" "<<i*i<<endl;
					count++;
				}
		}
		cout<<"Case #"<<copy-t<<": "<<count<<endl;
	}

}
