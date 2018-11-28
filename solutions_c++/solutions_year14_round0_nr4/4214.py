#include <bits/stdc++.h>
using namespace std;
int main() {
	int t,n,i; double a[1000],b[1000];pair <double, int> c[1000];
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>n;
		int j;
		for(j=0;j<n;j++)cin>>a[j];
		for(j=0;j<n;j++)cin>>b[j];
		sort(a,a+n);sort(b,b+n);
		for(j=0;j<n;j++){c[j].first=a[j];c[j].second=1;}
		for(j=n;j<2*n;j++){c[j].first=b[j-n];c[j].second=-1;}
		sort(c,c+2*n);
		cout<<"Case #"<<i<<": ";

		    long long an = 0, cr = 0, mx = -1, cur = 0;
		    for (j=0;j<2*n;++j){
		      if (c[j].second == -1) cr ++ ;
		      else if (cr>0){
			 cr--;   an++;
		      }
		    }
		    for (j=2*n-1;j>=0;--j){
		      cur+=c[j].second;
		      mx = max (mx, cur);
		    }
		    cout<<an << " "<< mx<<"\n";
	}
	return 0;
}
