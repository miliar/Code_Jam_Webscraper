#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;

#define all(x) x.begin(),x.end()

int n,k;
ld p[300];

ld r=1;

deque<ld> v;

ld s[301][301];

ld get()
{
	s[0][0]=1;

	for (int i=0; i<v.size(); i++)
	{
		s[i+1][0] = s[i][0]*v[i];
		s[0][i+1] = s[0][i]*(1-v[i]);
		for (int j=1; j<i+1; j++)
			s[j][i-j+1] = v[i]*s[j-1][i-j+1] + (1-v[i])*s[j][i-j];
	}

	return s[k/2][k/2];
}

int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0);


	int testc;
	cin>>testc;

	cout<<fixed<<setprecision(12);
	for (int tti=1; tti<=testc; tti++)
	{
		cout<<"Case #"<<tti<<": ";

		r=0;
		cin>>n>>k;

		for (int i=0; i<n; i++)
			cin>>p[i];

		sort(p,p+n);

		v.clear();

		for (int i=0; i<k; i++)
			v.push_back(p[k-1-i]);

		for (int i=0; i<k; i++)
		{
			r = max(r,get());
			v.pop_front();
			v.push_back(p[n-1-i]);
			r = max(r,get());
		}

		cout<<r;
		cout<<'\n';
		cerr<<"Case #"<<tti<<": DONE\n";
	}

    return 0;
}

