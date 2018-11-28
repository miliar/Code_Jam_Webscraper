#include <iostream>
using namespace std;
int main()
{
	int t,s_max,count,ans,i,j;
	string s;

	cin >> t;
	for(i=1;i<=t;i++)
	{
		count=0;
		ans=0;
		cin >> s_max >> s;
		for(j=0;j<=s_max;j++)
		{
			if(s[j]!=0)
			{
				if((j-count)>ans)
					ans=j-count;
				count+=s[j]-'0';
			}
		}
		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}