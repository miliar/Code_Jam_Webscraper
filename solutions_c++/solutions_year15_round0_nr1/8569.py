#include<iostream>

using namespace std;

int main()
{
	int t, n, i, x = 1;
	char shy[1005];
	
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	cin>>t;
	
	while(t--)
	{	
		cin>>n>>shy;
		
		long long int count = 0, frnd = 0;
		for(i=0;i<=n;i++)
		{
			if(shy[i]!='0')
			{
				if(count<i)
				{
					frnd += (i-count);
					count += (i-count);
				}
				int num = shy[i] - 48;
				count += num;
			}
		}
		cout<<"Case #"<<x<<": "<<frnd<<endl;
		x++;
	}
	
	return 0;
}
