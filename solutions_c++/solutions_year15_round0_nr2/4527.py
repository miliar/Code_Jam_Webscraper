#include <bits/stdc++.h>
using namespace std;
int f(vector<int> v,int ans)
{
	if(v[v.size()-1]==1)
		return ans+1;
	if(v[v.size()-1]==0)
		return ans;
	int r1=1000,r2;
	vector<int> v1;
	for(int i=0;i<v.size();i++)
		v1.push_back(v[i]-1);
	vector<int> v2;
	int xx=v[v.size()-1];
	for(int i=2;i<=xx/2;i++)
	{
		
		v2.clear();
		for(int j=0;j<v.size();j++)
		{
			v2.push_back(v[j]);
		}
		v2.pop_back();
		v2.push_back(xx/i);
		v2.push_back(xx-xx/i);
		sort(v2.begin(),v2.end());
		r1=min(r1,f(v2,ans+1));//special minute
	}
	
	r2=f(v1,ans+1);//not special minute
	return min(r1,r2);
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out3.txt", "w", stdout);
	int t;
	cin >> t;
	for (int test = 0; test < t; test++)
	{
		int d;
		vector <int> v;
		cin >> d;
		for (int i = 0; i < d; i++)
		{
			int temp;
			cin >> temp;
			v.push_back(temp);
		}
		// make_heap (v.begin(),v.end());
		sort(v.begin(), v.end());
		int ans = 0;
		ans=f(v,ans);

		cout << "Case #" << test + 1 << ": ";
		cout << ans << "\n";
	}
	return 0;
}