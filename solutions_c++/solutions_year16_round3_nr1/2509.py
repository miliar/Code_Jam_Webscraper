#include<iostream>
#include<vector>
#include<algorithm>
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
		int cou=0;
		vector<pair<int,char> >a(n);
		for(int i=0;i<n;i++)
			{	
				a[i].second=i+'A';
				cin>>a[i].first;
				cou+=a[i].first;
			}
		sort(a.begin(),a.end());
		cout<<"Case #"<<Case<<": ";
		Case++;
		bool f=0;
		while(a[n-1].first!=0)
		{
			if(a[n-1].first!=0)
			{
				cout<<a[n-1].second;
				a[n-1].first--;
				cou--;
			}
			sort(a.begin(),a.end());
			if(a[n-1].first!=0)
			{
				if(cou!=2 || f){
				cout<<a[n-1].second<<" ";
				a[n-1].first--;
				cou--;
				}
				else
				{
					cout<<" ";
					f=1;
				}
			}
			sort(a.begin(),a.end());
		}
		cout<<endl;
	}
	return 0;
}
