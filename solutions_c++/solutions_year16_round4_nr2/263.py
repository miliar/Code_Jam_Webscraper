#include <bits/stdc++.h>
using namespace std;
long double f(vector <long double> &A)
{
	int sz = A.size();
	vector <long double> P(sz+1, 0.0);
	P[0] = 1.0;
	for (int i = 0; i < sz; ++i)
	{
		vector <long double> temp(sz+1, 0.0);
		for (int j = 0; j <= i; ++j)
		{
			temp[j]+=P[j]*(1.0 - A[i]);
			temp[j+1]+=P[j]*A[i];
		}
		P = temp;
	}
	return P[sz/2];
}
int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.precision(10);
	int t;
	cin>>t;
	for (int tc = 1; tc <= t; ++tc)
	{
		int n,k;
		cin>>n>>k;
		vector <long double> prob(n);
		for (int i = 0; i < n; ++i)
			cin>>prob[i];
		sort(prob.begin(), prob.end());
		long double ans = 0.0;
		for (int i = 0; i < n; ++i)
		{
			vector <long double> temp;
			for (int j = 0; j < k; ++j)
				temp.push_back(prob[(i+j)%n]);
			ans = max(ans,f(temp));
		}
		cout<<"Case #"<<tc<<": "<<fixed<<ans<<"\n";
	}
	return 0;
}