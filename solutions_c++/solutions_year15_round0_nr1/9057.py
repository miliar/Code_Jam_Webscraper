#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("Ainput.txt","r",stdin);
    freopen("Ans1.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int p=1;p<=t;p++)
	{
		long long frns=0,ppl=0,x;
		int maxs,i;
		scanf("%d",&maxs);
		string a;
		cin>>a;
		ppl=(long long)a[0]-48;

		for(long long i=1;i<=maxs;i++)
		{
			if(i>ppl)
			{
				x=i-ppl;

				frns+=i-ppl;

				ppl+=(long long)a[i]-48+x;
			}
			else
			{
				ppl+=(long long)a[i]-48;
			}
		}
		printf("Case #%d: %lld\n",p,frns);
	}
    return 0;
}
