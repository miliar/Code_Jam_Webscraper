#include<fstream>
using namespace std;
ifstream cin("input.txt");
ofstream cout("output.txt");
int main()
{
	int t,q,ans,ans1,i,a[1005],lvl,n;
	cin >> t;
	for(q=1;q<=t;q++)
	{
		cin >> n;
		ans=1001;
		ans1=0;
		for (i=1;i<=n;i++)
		{
			cin >> a[i];
		} 
		for(lvl=1;lvl<=1000;lvl++)
		{
			ans1=lvl;
			for(i=1;i<=n;i++)
			{
				if (a[i]>lvl)
				{
				ans1+=(a[i]/lvl-1+((a[i]%lvl==0)? 0:1));
			    }
			}
			if (ans1<ans)
			{
				ans=ans1;
			}
		}
		cout << "Case #" << q << ": " << ans << "\n";
	}
	return 0;
}
