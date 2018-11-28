#include <bits/stdc++.h>

using namespace std;
set<int>save;
long long n;
int main(void)
{
	int test;
	scanf("%d",&test);

	for(int t=1; t<=test; t++)
	{
		cin>>n;
		save.clear();
		if(n==0) printf("Case #%d: INSOMNIA\n",t);
		else
		{
			int mul=1;
			int temp=n;
			while(1)
			{
				int res=temp;
				while(temp)
				{
					save.insert(temp%10);
					temp/=10;
				}
				if(save.size()==10) {cout<<"Case #"<<t<<": "<<res<<endl;break;}
				temp=n*(++mul);
			}
		}

	}	
	return 0;
}