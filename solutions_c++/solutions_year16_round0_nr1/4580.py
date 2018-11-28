/*
coded by @just_code21
© to Prakhar Srivastava
*/
#include<bits/stdc++.h>
#define ll long long int
#define M 1000000007
using namespace std;

int main()
{
	ifstream fin("inpp.in");
	ofstream fout("output.txt");
	int t;
	fin>>t;
	//scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		int n,count=0,power=0;
		fin>>n;
	//	scanf("%d",&n);
		if(n==0)
		{
			fout<<"Case #"<<i<<": INSOMNIA\n";
		//	printf("Case #%d: INSOMNIA\n",i);
			continue;
		}
		int hash[10]={0};
		while(count<10)
		{
			power++;
			int temp=n*power;
			while(temp>0)
			{
				int last=temp%10;
				temp/=10;
				if(hash[last]==0)
				{
					hash[last]++;
					count++;
				}
			}
		}
		fout<<"Case #"<<i<<": "<<n*power<<"\n";
	//	printf("Case #%d: %d\n",i,n*power);
	}
	return 0;
}
/*

*/


