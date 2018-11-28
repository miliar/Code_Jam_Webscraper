#include <bits/stdc++.h>

using namespace std;
int main()
{
	//ifstream cin("in.txt");
	//ofstream cout("out.txt");
	int T;
	cin>>T;
	for (int j=1;j<=T;j++)
	{
		cout<<"Case #"<<j<<": ";
		
		string s;
		cin>>s;

		int cost = 0;
		for (int i=0;i<s.length()-1;i++)
		if (s[i]!=s[i+1]) cost++;


		if (s[0]=='+')
		{
			if (cost%2==1) cost++;				
		} else if (cost%2==0) cost++;

		cout << cost << endl;
	}

	return 0;
}
