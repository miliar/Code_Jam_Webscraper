#include <iostream>
#include <algorithm>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <vector>

using namespace std;

int t, kol, n, ans1, ans2, o;
long double a[11], b[11], eps=1e-7;
int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	cin>>t;
	for(int kol=1;kol<=t;kol++)
	{
		cin>>n;
		for(int i=0;i<n;i++)
			cin>>a[i];
		for(int i=0;i<n;i++)
			cin>>b[i];
		cout<<"Case #"<<kol<<": ";
		ans1=0;
		ans2=100;
		vector<int> v;
		o=1;
		for(int i=1;i<=n;++i)
		{
			v.push_back(i);
			o*=i;
		}
		while(o--)
		{
			int k=0;
			for(int i=0; i<n; ++i)
				if (a[i]-eps>b[v[i]-1])
					k++;
			ans1=max(ans1, k);
			ans2=min(ans2, k);
			next_permutation(v.begin(), v.end());
		}
		cout<<ans1<<" "<<ans2<<endl;
	}
	return 0;
}