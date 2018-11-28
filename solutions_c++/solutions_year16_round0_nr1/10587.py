#include<iostream>
#include<cstring>
using namespace std;
typedef long long ll;
int main()
{
	ll n;
	int t,count;
	cin>>t;
	int k = 1;
	ll flag,change;
	int arr[10];
	while(t--)
	{
		
		count = 0;
		change = 0;
		for(int j=0;j<10;j++)
		{
			arr[j] = 0;
		}
		cin>>n;
		if(n==0)
		{
			cout << "Case #" << k++ << ": " "INSOMNIA";
			cout<<endl;
			continue;
		}
		ll temp = n;
		ll i;
		for(i=1;count<10;i++)
		{
			temp = n*i;
			while(temp>0)
			{
				change = 0;
				if(arr[temp%10]==0)
				{
					arr[temp%10] = 1;
					count++;
					change = 1;
				}
				temp = temp/10;
			}
		}
		cout << "Case #" << k++ << ": " << n*(i-1) << endl; 
	
	}
}
