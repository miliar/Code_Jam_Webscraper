#include<iostream>
#include<vector>
using namespace std;
int main()
{
	ios_base::sync_with_stdio(0);
	int t;
	cin>>t;
	long long n;
	int Case=1;
	while(t--)
	{
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<Case<<": INSOMNIA"<<endl;
			Case++;
			continue;
		}
		vector<int>a(10,0);
		bool f=1;
		long long te=n;
		long long N=n;
		long long I=2;
		while(f)
		{
			te=n;
			while(te!=0)
			{
				a[te%10]=1;
				te/=10;
			}
			for(int i=0;i<10;i++)
				{
					if(a[i]==0)
					{
						n=N*I;
						I++;
						f=1;
						break;
					}
					f=0;
				}
		}
		cout<<"Case #"<<Case<<": "<<n<<endl;
		Case++;
	}
	return 0;
}
