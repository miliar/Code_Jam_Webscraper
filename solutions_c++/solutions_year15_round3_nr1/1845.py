#include<fstream>
#include<string>
#include<cmath>
#include<algorithm>
using namespace std;
ifstream cin("input.txt");
ofstream cout("output.txt");
int main()
{
	int t,q,r,c,w,ans;
	cin >> t;
	for (q=1;q<=t;q++)
	{
		cin >> r >> c >> w;
		ans=c/w;
		/*if (c%w!=0)
		{
			ans++;
		}*/
		ans+=w-1;
		if ((c/w)*w<c) ans++;
		ans=ans*r;
    	cout << "Case #" << q << ": " << ans << "\n";
	}
	return 0;
}
