#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	int T;
	string ans,S;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		cin>>S;
		ans = "";
		ans = ans + S[0];
		for(int i=1;i<S.length();i++)
		{
			if(S[i]>=ans[0])
			{
				ans = S[i] + ans; 
			}
			else
			{
				ans = ans + S[i];
			}
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}