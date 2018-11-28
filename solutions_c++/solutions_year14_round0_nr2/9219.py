#include<iostream>
#include<algorithm>
#include<vector>
#include<iomanip>
using namespace std;

int main()
{
	int T;
	cout << fixed << setprecision(7);
	cin >> T;
	for (int x=1;x<=T;x++)
	
	{
		long double C,F,X;
		cin >> C >> F >> X;
		int nf=0;
		long double tbb=0.0;
		long double ans=X/2;
		while(1)
		{
			
			tbb+=(C)/(2+F*nf);
			nf++;
			long double curr=tbb+X/(2+F*nf);
			if (curr>ans) break;
			ans=min(ans, tbb+X/(2+F*nf));
			
		}
		cout << "Case #" << x << ": " << ans << endl;
	}
}
