#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;

#define all(x) x.begin(),x.end()

#define mp make_pair

int n,r,p,s;

map<pair<pair<int,int>,pair<int,int>>,string> m;

//R-0 P-1 S-2

void ini()
{
	struct t
	{
		int x,y,z;
		int w;
		string p;
	};

	vector<t> v;

	v.push_back({1,0,0,0,"R"});
	v.push_back({0,1,0,1,"P"});
	v.push_back({0,0,0,2,"S"});

	for (int i=1; i<=13; i++)
	{
		for (t j:v)
			m[mp(mp(j.x,j.y),mp(j.z,j.w))] = j.p;

		vector<t> vv;
		for (int j=0; j<v.size(); j++)
			for (int k=j+1; k<v.size(); k++)
			{
				t x=v[j],y=v[k];
				if ((x.w+1)%3 != y.w) swap(x,y);
				if (x.w==y.w) continue;
				int w = y.w;
				if (x.p>y.p) swap(x,y);
				vv.push_back({x.x+y.x,x.y+y.y,x.z+1,w,x.p+y.p});
			}
		v=vv;
	}
}

int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0);

	ini();

	int testc;
	cin>>testc;
	for (int tti=1; tti<=testc; tti++)
	{
		cout<<"Case #"<<tti<<": ";

		cin>>n>>r>>p>>s;


		bool f=0;
		for (int i=0; i<3 && !f; i++)
			if (m[mp(mp(r,p),mp(n,i))]!="") cout<<m[mp(mp(r,p),mp(n,i))],f=1;

		if (!f) cout<<"IMPOSSIBLE";
		cout<<'\n';
		cerr<<"Case #"<<tti<<": DONE\n";
	}

    return 0;
}

