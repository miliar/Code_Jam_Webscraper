#include <iostream>
using namespace std;

string s;

int main() {
	int t;
	cin >> t;
	for(int tt = 1; tt <= t ;tt++)
	{
		int n;
		cin >> n >> s;
	//	cout << n <<" "<< s<<endl;
		int cnt = 0;
		int ans =0;
		cnt += s[0]-'0';
		for(int i = 1 ; i <= n;i++)
		{
			if(s[i] == '0')
				continue;
			if(cnt >= i)
				cnt += s[i]-'0';
			else
				{
				//	cout << i << " " << cnt << endl;
					ans += i-cnt;
					cnt += i-cnt;
					cnt +=s[i]-'0';
				}
		}
		cout <<"Case #"<<tt<<": "<< ans << endl;
	}
	return 0;
}