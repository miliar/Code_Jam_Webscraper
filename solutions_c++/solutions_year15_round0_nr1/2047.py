#include <iostream>
#define ll long long
using namespace std;

int main() 
{
	int t;
	scanf("%d",&t);
	for(int k=1;k<=t;k++)
	{
		int n,j;
		scanf("%d",&n);
		char s[1005];
		scanf("%s",s);
		n+=1;
		int i;
		ll sum1=0,sum=0;
		for(i=0;i<n-1;i++)
		{
			sum1+=s[i]-48;
			if(sum1<(i+1))
			{
				sum++;
				sum1++;
			}
		}
		cout<<"Case #"<<k<<": "<<sum<<endl;
	}
	return 0;
}
