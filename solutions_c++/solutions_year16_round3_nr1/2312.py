#include <iostream>
using namespace std;

int main() {
	int t,n,count;
	cin>>t;
	for(int i = 1; i <= t; i++)
	{
		cin>>n;
		int a[n] = {0};
		count = 0;
		cout<<"Case #"<<i<<": ";
		for(int j = 0; j < n; j++)
		{
			cin>>a[j];
			count += a[j];
		}
		while(count > 0)
		{
			int max = 0;
			int index;
			int my = 0;
			char ans;
			int index1;
			index = 0;
			for(int k = 0; k < n; k++)
			{
				if(a[k])
					my++;
				if(a[k] > max)
				{
					max = a[k];
					index = k;
				}
			}

			if(my > 2)
			{
				a[index]--;
				count--;
				ans = 'A' + index;
				cout<<ans<<" ";
			}
			else
			{
				int q = 0;
				for(int p = 0; p < n; p++)
				{
					if(a[p])
					{
						if(q == 0)
						{
							index = p;
							q++;
						}
						else
						{
							index1 = p;
						}
					}
				}
				if(a[index] > a[index1])
				{
					a[index]--;
					count--;
					ans = 'A' + index;
					cout<<ans<<" ";
				}
				else if(a[index] < a[index1])
				{
					a[index1]--;
					count--;
					ans = 'A' + index1;
					cout<<ans<<" ";
				}
				else
				{
					a[index]--;
					a[index1]--;
					count--;
					count--;
					ans = 'A' + index;
					char ans1 = 'A' + index1;
					string b = "";
					b = b + ans;
					b = b + ans1;
					cout<<b<<" ";
				}
				
			}
		}
		cout<<endl;
	}
	return 0;
}