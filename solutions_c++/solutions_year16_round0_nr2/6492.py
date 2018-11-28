#include <bits/stdc++.h>
#define llong long long

using namespace std;
int main()
{
	//ifstream cin("in.txt");
	//ofstream cout("out.txt");
	int T;
	cin>>T;
	for (int Q=1;Q<=T;Q++)
	{
		cout<<"Case #"<<Q<<": ";
		
		string s;
		cin>>s;

		int moves = 0;
		for (int i=0;i<s.length()-1;i++)
		if (s[i]!=s[i+1]) moves++;


		if (s[0]=='+')
		{
			if (moves%2==1) moves++;				
		} else if (moves%2==0) moves++;

		cout << moves << endl;
	}

	return 0;
}
