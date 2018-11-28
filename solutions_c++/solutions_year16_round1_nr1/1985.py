#include <iostream>
#include <string>

using namespace std;

int case_i, case_n;

int main()
{
	string s,ans="";
	int l;
	cin >> case_n;
	for (case_i = 1; case_i <= case_n; case_i++){
		ans = "";
		cin >> s;
		l = s.length();
		ans = ans + s[0];
		for (int i=1;i<l;i++)
		{
			if (s[i] >= ans[0])
			{
				ans = s[i] + ans;
			}
			else
			{
				ans = ans + s[i];
			}
		}
		cout << "Case #"<<case_i<<": "<< ans << endl;
	}
	return 0;
}