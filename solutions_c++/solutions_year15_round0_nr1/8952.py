#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
	//freopen("1.txt","r",stdin);
	//freopen("2.txt","w",stdout);
	int t,n,sma;
	string a;
	int b[2000];
	cin>>t;

	for (int t1 = 1; t1 <= t ; ++t1)
	{
		cin>>n;
		cin>>a;
		b[0]=0;
		sma=0;
		for (int i = 1; i <= n; ++i)
		{
			b[i]=a[i-1]-'0'+b[i-1];
			//cout<<b[i]<<" ";
			sma=max(sma,i-b[i]);
		}
		cout<<"Case #"<<t1<<": ";
		cout<<sma<<endl;
	}
	
}