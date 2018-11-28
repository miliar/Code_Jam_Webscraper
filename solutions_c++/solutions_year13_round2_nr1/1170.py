#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
using namespace std;
int main()
{
	long long i,t,j,k,a,n,cnt,ans;
	vector<long long>arr;
	//fstream cin;
	//cin.open("C:\\Users\\Sushrut\\Desktop\\Google Code Jam\\2013\\Round 1B\\A\\Small Input.txt",ios::in);
	//freopen("C:\\Users\\Sushrut\\Desktop\\Google Code Jam\\2013\\Round 1B\\A\\Small Output.txt","w",stdout);
	cin>>t;
	for(k=1;k<=t;k++)
	{
		cin>>a>>n;
		arr.clear();
		ans=n;
		cnt=0;
		i=n;
		while(i--)
		{
			cin>>j;
			arr.push_back(j);
		}
		sort(arr.begin(),arr.end());
		if(a==1&&arr[0]==1)
		{
			ans=n;
		}
		else
		{
			cnt=0;
			for(i=0;i<n;i++)
			{
				if(arr[i]<a)
					a+=arr[i];
				else
				{
					while(a<=arr[i])
					{
						a=a*2-1;
						cnt++;
					}
					a+=arr[i];
				}
				if(ans>(cnt+n-i-1))
					ans=cnt+n-1-i;
			}
		}
		cout<<"Case #"<<k<<": "<<ans<<endl;
	}
	return 0;
}