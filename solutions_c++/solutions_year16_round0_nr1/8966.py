#include<bits/stdc++.h>
#define ll long long int
using namespace std;

int main()
{
	ll test;
	scanf("%lld",&test);
	ll tr=test;
	while(test--)
	
	{
		ll i;
		scanf("%lld",&i);
		ll steps=0;
		int arr[10];
		for(int j=0;j<10;++j)
				arr[j]=0;
		ll st=i;
		ll    cnt=0;
		ll temp=st;
		while(cnt<10&&i!=0)
		{
			//cout << cnt << "\n";
			temp=st;
			++steps;
			
			while(temp>0&&cnt<10)
			{
				if(arr[temp%10]==0)
			{	arr[temp%10]=1;
				++cnt; 
			}
				temp=temp/10;
			}
			st+=i;

		}
		printf("Case #");
		printf("%lld",tr-test);
		printf(": ");
		if(i==0)
			printf("INSOMNIA");
		else
			printf("%lld",st-i);
		printf("\n");

	}


}