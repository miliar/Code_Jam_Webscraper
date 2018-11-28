#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;

struct node {
	double r,c;

	node(double _r,double _c) {
		r=_r,c=_c;
	}

	node() {
		r=0,c=0;
	}
};

int tt;
int n;
double x,v;
vector<node> a,b,c;

double calc(double mid) {
	double sum=0,sum1=0;
	double res=0;
	for (int i=0;i<(int)a.size();++i) {
		sum+=mid*a[i].r*a[i].c;
		res+=mid*a[i].r;
	}
	for (int i=0;i<(int)b.size();++i) {
		sum1+=mid*b[i].r*b[i].c;
		res+=mid*b[i].r;
	}
	for (int i=0;i<(int)c.size();++i)
		res+=mid*c[i].r;
	if (sum>sum1) {
		for (int i=0;i<(int)a.size();++i)
			if (sum-mid*a[i].r*a[i].c<sum1+1e-10) {
				double tmp=(sum-sum1)/a[i].c;
				res-=tmp;
				break;
			} else {
				sum-=mid*a[i].r*a[i].c;
				res-=mid*a[i].r;
			}
	} else {
		for (int i=0;i<(int)b.size();++i)
			if (sum1-mid*b[i].r*b[i].c<sum+1e-10) {
				double tmp=(sum1-sum)/b[i].c;
				res-=tmp;
				break;
			} else {
				sum1-=mid*b[i].r*b[i].c;
				res-=mid*b[i].r;
			}
	}
	return res;
}

bool cmp(const node &a,const node &b) {
	return a.c>b.c;
}

int main() {
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);

	cin >> tt;
	for (int ii=1;ii<=tt;++ii) {
		cin >> n >> v >> x;
		a.clear(); b.clear(); c.clear();
		for (int i=0;i<n;++i) {
			double p,q;
			cin >> p >> q;
			if (q==x) c.push_back(node(p,0));
			else {
			if (q>x) a.push_back(node(p,q-x));
			else b.push_back(node(p,x-q));
			}
		}

		printf("Case #%d: ",ii);
		if ((a.size()==0 || b.size()==0) && c.size()==0) {
			printf("IMPOSSIBLE\n");
			continue;
		}

		sort(a.begin(),a.end(),cmp);
		sort(b.begin(),b.end(),cmp);

		double l=0,r=100000000;
		while (r-l>1e-8) {
			double mid=(l+r)/2;
			if (calc(mid)>v) r=mid;
			else l=mid;
		}

		printf("%.10f\n",l);
	}
}
