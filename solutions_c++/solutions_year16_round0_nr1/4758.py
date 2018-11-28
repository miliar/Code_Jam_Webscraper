#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t, n, a, b, c, i, num, flag, Count;
	int visited[12];
	
	Count=1;
	cin>>t;
	while(t--)
	{
		flag=0;
		memset(visited, 0, 4*12);
		cin>>n;
		a=1;

		if(n==0)
			cout<<"Case #"<<Count<<": "<<"INSOMNIA\n";
		else
		{
			while(flag!=1)
			{
				b = a*n;

				while(b)
				{
					visited[b%10]=1;
					b=b/10;
				}

				for(i=0; i<10; i++)
				{
					if(visited[i]==0)
						break;
				}
				if(i==10)
				{
					flag=1;
					num = a*n;
				}
				a++;
			}
			cout<<"Case #"<<Count<<": "<<num<<endl;
		}
		Count++;
	}
	return 0;
}