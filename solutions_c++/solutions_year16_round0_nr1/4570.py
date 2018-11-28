#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,t1=0;
	scanf("%d",&t);
	while(t--)
	{
		t1++;
		int n;
		scanf("%d",&n);
		set<int>s;
		int a[11];
		for(int i=0;i<10;i++)a[i] = 0;
			int cnt = 0;
		int d = 0;
		int flag=0;
		while(1)
		{
			int new_val = (d+1)*n;
			if(s.find(new_val)!=s.end())
			{
				// exits
				flag=1;
				break;
			}
			else{
				s.insert(new_val);
				while(new_val>0)
				{
					int dig = new_val%10;
					new_val /= 10;
					if(!a[dig])
					{
						cnt++;
						a[dig]++;
					}
					if(cnt==10)
						break;
				}
				d++;
			}
			if(cnt==10)break;
		}

		if(flag)
		{
			printf("Case #%d: INSOMNIA\n",t1);
		}
		else 
			printf("Case #%d: %d\n",t1,d*n);
	}
	return 0;
}