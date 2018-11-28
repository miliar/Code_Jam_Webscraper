#include<iostream>
#include<algorithm>

using namespace std;
int main()
{
	remove("output.txt");
	freopen("A-large.in","r", stdin);
	freopen("output.txt","w", stdout);
	int t;
	cin>>t;
	
	int smax;
	char c;
	int sum = 0;
	int max = 0;
	int val;
	
	for(int i = 0; i < t; ++i)
	{
		max = 0;
		cin>>smax;
		int a[smax + 1];
		
		for(int i = 0; i <= smax; ++i)
			{
				cin>>c;
				a[i] = c - '0';
			}
		
		for(int i = 1; i <= smax; ++i)
			{	
				sum = 0;
				for(int j = 0; j < i; ++j)
					{
						sum += a[j];
					}
				val = i - sum;
				if(val < 0)
					val = 0;
				
				if(val > max)
					max = val;
			}
		
		cout<<"Case #"<<(i + 1)<<": "<<max<<"\n";
	}
	
	
}
