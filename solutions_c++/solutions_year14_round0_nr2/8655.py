#include <bits/stdc++.h>

using namespace std;

int main()
{
	int T;
	cin>>T;
	for (int i = 0; i < T; ++i)
	{
		double C,F,X;
		cin>>C>>F>>X;
		double Csum = C/2;
		double prev = X/2;
		int num = 1;
		while(true)
		{
			double ans = X/(num*F+2);
			ans+=Csum;
/*			cout<<ans<<endl;
*/			if(ans > prev)
			{
				cout<<"Case #"<<i+1<<": ";
				cout<<setprecision(7)<<fixed<<prev<<endl;
				break;
			}
			prev = ans;
			Csum +=C/(num*F+2);
			num++;
		}
		
	}
}