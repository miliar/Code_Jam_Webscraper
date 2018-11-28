#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;

#define all(x) x.begin(),x.end()

int n;
int a[25];

int r=0;

int b[25];

int oc[4];
int w[4];

bool f=1;

void goc(int x)
{
	bool g=0;
	if (x==n) return;
	for (int i=0; i<n; i++)
		if ((b[w[x]]>>i)%2 && oc[i]==0) 
		{
			g=1;
			oc[i]=1;
			goc(x+1);
			oc[i]=0;
		}
	f &=g;
}

void gob()
{
	for (int i=0; i<n; i++)
		oc[i]=0,w[i]=i;
		
	f=1;
	do
	{
		goc(0);	
	} while (next_permutation(w,w+n));
	
	if (!f) return;
	
	int t = 0;
	for (int i=0; i<n; i++)
	{
		if ((a[i] | b[i]) != b[i]) f=0;
		t+=__builtin_popcount(b[i]^a[i]);
	}
	if (!f) return;
	
	r = min(r,t);
}

void goa(int l)
{
	if (l==n) gob();
	else
	for (int i=0; i<(1<<n); i++)
		b[l] = i,goa(l+1);
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

		r=20;
		cin>>n;
		
		for (int i=0; i<n; i++)
		{
			a[i]=0;
			char c;
			for (int j=0; j<n; j++)
				cin>>c,a[i] = a[i]*2+c-'0';
		}	
		
		goa(0);
		
		cout<<r;
		cout<<'\n';
		cerr<<"Case #"<<tti<<": DONE\n";
	}

    return 0;
}

