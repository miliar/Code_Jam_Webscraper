#include<iostream>
#include<algorithm>
#include<vector>
#define pb push_back
using namespace std;
int a[2505];
vector<int>vec;
void reset()
{
	for(int i =0 ;i<2505;i++)
	a[i] = 0;
}
int main()
{
	int t , n , temp ,p =0;
	cin>>t;
	while(t--)
	{
		p++;
		vec.clear();
		reset();
		cin>>n;
		for(int i=0;i<2*n-1;i++)
		{
			for(int j =0 ;j<n;j++)
			{
				cin>>temp;
				a[temp]++;
			}
		}
		for(int i =0 ;i<2505;i++)
		{
			if(a[i]&1)
			vec.pb(i);
		}
		cout<<"Case #"<<p<<": ";
		sort(vec.begin(),vec.end());
		for(int i =0 ;i<vec.size();i++)
		cout<<vec[i]<<" ";
		cout<<endl;
	}
}
