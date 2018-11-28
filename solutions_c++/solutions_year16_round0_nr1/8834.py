#include<bits/stdc++.h>
using namespace std;
int main()
{
	int tc,n,ans,cnt,array[10],temp,now;
	cin >> tc;
	for(int x=1;x<=tc;x++)
	{
		cin >> n;
		cnt=0;
		for(int i=0;i<10;i++)
			array[i]=0;
		if(n==0)
		{
			cout << "Case #" << x << ": " <<  "INSOMNIA\n";
		}
		else
		{
			ans=0;
			now=n;
			while(cnt<10)
			{
				temp=now;
				while(temp>0)
				{
					array[temp%10]=1;
					temp/=10;
				}
				cnt=0;
				for(int i=0;i<10;i++)
				{
					if(array[i])
						cnt++;
				}
				ans++;
				now+=n;
			}
			cout << "Case #" << x << ": " << now-n << "\n";
		}
	}
	return 0;
}
