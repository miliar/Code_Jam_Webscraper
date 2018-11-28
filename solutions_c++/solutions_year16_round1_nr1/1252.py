#include<bits/stdc++.h>

using namespace std;

string s;

int main()
{
	int nt;
	scanf(" %d",&nt);
	for(int t=1; t<=nt; t++)
	{
		string r = "";
		cin >> s;
		r = r+s[0];
		for(int i=1; s[i]; i++)
			if(s[i]>=r[0]) r = s[i] + r;
			else r = r + s[i];
		cout << "Case #" << t << ": " << r << endl;
	}
	return 0;
}
