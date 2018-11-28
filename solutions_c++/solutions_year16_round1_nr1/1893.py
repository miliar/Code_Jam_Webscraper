
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int tt;
string cur,ans;

int main()
{
	freopen("al.in","r",stdin);
	freopen("al.out","w",stdout);

	cin >> tt;
	for (int ii=1;ii<=tt;++ii)
	{
	    cin>>cur;
	    ans = cur[0];

			for (int jj = 1; jj <cur.length(); ++jj)
				{
					if (cur[jj] < ans[0])
					ans = ans + cur[jj];
					else
					ans = cur[jj] + ans;
				}





        cout<<"Case #" <<ii<<": "<<ans<<endl;
        //printf("Case #%d: %s\n",ii,ans);
	}
	return 0;
}
