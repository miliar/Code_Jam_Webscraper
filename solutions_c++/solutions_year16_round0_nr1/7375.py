#include <bits/stdc++.h>

using namespace std;


int main(int argc, char const *argv[])
{
	int T;
	long long int N;

	scanf("%d",&T);
	for(int k=0;k<T;k++)
	{
		scanf("%lld",&N);
		if(N==0)
		{
			printf("Case #%d: INSOMNIA\n",k+1);
			continue;
		}
		int arr[11];
		for(int i=0;i<10;i++)
			arr[i]=0;
		int ch=0;
		long long temp=N;
		long long int l=0;
		while(ch<10)
		{
			l++;
			temp=N*l;
			while(temp!=0)
			{
				int a=temp%10;
				if(arr[a]==0)
				{
					ch++;
					arr[a]=1;
				}
				temp/=10;
				if(ch>=10)
					break;
			}
		}
		printf("Case #%d: %lld\n",k+1,l*N);		
	}
	return 0;
}