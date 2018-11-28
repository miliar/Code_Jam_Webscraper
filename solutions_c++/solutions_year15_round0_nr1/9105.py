#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main()
{
	freopen("a.in","r",stdin);
	freopen("b.txt","w",stdout);
	int tnum;
	int q = 1;
	cin>>tnum;
	while(tnum--)
	{
		int n;
		string s;
		cin>>n >> s;
		int cnt = s[0]-'0';
		int ans = 0;
		for(int i=1;i<s.size();i++)
		{
			if(cnt < i)
			{
				ans += i - cnt;
				cnt += i - cnt;
			}
			int x = s[i]-'0';
			cnt += x;
		}
		cout << "Case #" << q++ << ": " << ans << endl;
	}
}