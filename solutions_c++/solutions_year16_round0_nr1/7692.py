#include<bits/stdc++.h>

using namespace std;

int main()
{
	freopen("0.in","r",stdin);
	freopen("op.txt","w",stdout);
	long long t,count,c=1,a[10],k,m;
	cin >> t;
	while(c<=t)
	{
		count=0;
		for(int i=0;i<10;i++)
		{
			a[i]=i;
		}
		long long n;
		cin >> n;
		if(n==0)
			cout << "Case #" << c <<": "<< "INSOMNIA" << endl;
		else
		{
			for(int i=1;i<=1000000;i++)
			{
				k=i*n;
				while(k!=0)
				{
					m=k%10;
					for(int j=0;j<=9;j++)
					{
						if(m==a[j])
						{
							count++;
							a[j]=10;
							break;
						}
					}
					k/=10;
				}
				if(count==10)
				{
					cout << "Case #" << c << ": " << i*n << endl;
					break;
				}
			}

		}

		c++;
	}
	return 0;

}
