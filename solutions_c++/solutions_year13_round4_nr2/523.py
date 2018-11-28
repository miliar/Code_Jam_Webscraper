#include <fstream>
#include <cstdio>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;

struct node
{
	int id,data;
	bool f;
};

node a[40000];
long long v[40000];
const int p=1000002013;

bool cmp(node x,node y)
{
	if (x.id<y.id||((x.id==y.id)&&(!y.f)&&(x.f))) 
		return true;
	else
		return false;
}

long long ans;

int main()
{
	string input="A-small-attempt0 (3).in",output="1.out";
	ifstream infile("B-large (2).in",ios::in);
	ofstream oufile("1.out",ios::out);
	int tt;
	long long t,p,k,nn,ans1,ans2;
	int n,m;
	int l,r;
	infile>>tt;
	for (int loop=1;loop<=tt;loop++)
	{
		infile>>n>>p;
		nn=1;
		for (int i=0;i<n;i++) nn*=2;
		if (p==nn)
		{
			ans1=nn-1;
			ans2=nn-1;
		}
		else
		{
			t=nn-p;
			k=1;
			m=0;
			while (k<=t) 
			{
				k*=2;
				m++;
			}
			k=k/2;
			m--;
			k=nn/k;
			ans1=k-2;
			t=nn-t;
			k=1;
			m=0;
			while (k<=t) 
			{
				k*=2;
				m++;
			}
			k=k/2;
			m--;
			k=nn/k;
			ans2=nn-k;
		}
		oufile<<"Case #"<<loop<<": "<<ans1<<' '<<ans2<<endl;
	}
}
