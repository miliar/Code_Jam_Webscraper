#include<iostream>
using namespace std;
int exist[10];
void reset()
{
	for(int i=0;i<10;i++)
	exist[i] = 0;
}
int main()
{
	int t , n , k , coun = 0 , d;
	cin>>t;
	while(t--)
	{
		coun++;
		cin>>n;
		if(n == 0)
		{
			cout<<"Case #"<<coun<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		else
		{
			reset();
			int ans = 0 , counter = 0;
			for(int i = 1;;i++)
			{
				ans = i*n;
				k = ans;
				//cout<<k<<endl;
				while(k!=0)
				{
					d = k%10;
					if(exist[d] == 0)
					{
						counter++;
						exist[d] = 1;
					}
					k = k/10;
				}
				if(counter == 10)
				break;
			}
			cout<<"Case #"<<coun<<": "<<ans<<endl;
		}
	}
}
