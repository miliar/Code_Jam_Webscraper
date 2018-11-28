#include <iostream>
#include <cstdio>
#include <cstring>
#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

int n,m,aa,bb,cc,k;
double a[20];
vector<int> v,u;
vector<float> b;

int main(){
	int T;
	cin >> T;
	for (int ti=1;ti<=T;ti++){
		scanf("%d%d",&n,&k);
		cout <<"Case #"<< ti<<": ";
		for (int i=0;i<n;i++) scanf("%lf",&a[i]);
		v.clear();
		u.clear();
		for (int i=0;i<(1<<n);i++){
			int x = __builtin_popcount(i);
			if (x==k) v.push_back(i);
			if (i<(1<<k) && x==k/2) u.push_back(i);
		}
		//for (int i=0;i<v.size();i++) cout<<v[i]<<endl;
		//for (int i=0;i<u.size();i++) cout<<"!"<<u[i]<<endl;

		double ans=0;
		for (int i=0;i<v.size();i++){
			b.clear();
			int zz=v[i];
			for (int j=0;j<n;j++){
				if ((zz>>j) & 1) b.push_back(a[j]);
			}
			//for (int j=0;j<k;j++) cout<<b[j]<<" ";cout<<endl;
			assert(b.size()==k);
			double now=0;
			for (int j=0;j<u.size();j++){
				int xx=u[j];
				double cnt=1;
				for (int l=0;l<k;l++)
					if ((xx>>l) & 1) cnt*=b[l];
						else cnt*=1-b[l];
				now+=cnt;	
			}
			if (ans<now) ans=now;
		}
		printf("%.8f\n",ans);
		//cout<<ans<<endl;
	}
	return 0;
}
