#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
using namespace std;

int T;
string S;

void solve()/////////////////////////////////////
{
	int len = S.size();

	string ans;
	for(int i=0;i<len;i++)
	{
		if(ans.size()==0 || ans[0]>S[i])
			ans += S[i];
		else
		{
			string tmp = ""; 
			tmp += S[i];
			ans.insert(0,tmp,0,1);
		}
	}

	cout << ans << endl;
}

int main()///////////////////////////////////////
{
//	freopen("..\\input.txt","r",stdin);

//	freopen("..\\A-small-attempt0.in","r",stdin);
//	freopen("..\\A-small-attempt0.out","w",stdout);

	freopen("..\\A-large.in","r",stdin);
	freopen("..\\A-large.out","w",stdout);

	cin >> T;

	for(int id=1;id<=T;id++)
	{
		cin >> S;

		printf("Case #%d: ",id);

		solve();
	}
	return 0;
}