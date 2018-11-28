#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

int main()
{
	int tc, t, n, i, j, nf, ne, kf, ke, opt, dopt;
	double wn[1003], wk[1003];

	freopen("D.deceitful_war.in","r",stdin);
	freopen("D.out","w",stdout);

	cin>>tc;
	for(t=1; t<=tc; t++)
	{
		cin>>n;
		for(i=0; i<n; i++)
			cin>>wn[i];
		for(i=0; i<n; i++)
			cin>>wk[i];

		sort(wn,wn+n);
		sort(wk,wk+n);

		kf=nf=0;
		ne=ke=n-1;
		opt=0;
		while(kf<=ke && ne>=0)
		{
			if(wn[ne]>wk[ke]) {
				opt++;
				kf++;
			}
			else
				ke--;
			ne--;
		}

		//cout<<"Optimal: "<<opt<<endl;

		ne=ke=n-1;
		nf=kf=0;
		dopt=0;
		while(nf<=ne && ke>=0)
		{
			if(wn[ne]>wk[ke]) {
				dopt++;
				ne--;
			}
			else
				nf++;
			ke--;
		}

		cout<<"Case #"<<t<<": "<<dopt<<" "<<opt<<endl;
	}

	return 0;
}