#include <bits/stdc++.h>

using namespace std;

int main()
{
	freopen("A-large.in.txt" , "r" ,stdin);
	freopen("A-large.txt" , "w" ,stdout);
	int T;
	string s;
	cin >> T;
	for(int i = 1; i <= T ; i++)
	{	int n;
		cin >> n;
		cin >> s;
		int before = 0;
		int out = 0;
		for(int i = 0 ; i < s.size() ; i++)
		{
			if(before < i && s[i] > '0')
			{
			   out += min(1000,i - before);
			   before += min(1000 , i - before);
			   before += s[i] - '0';	 
			}else
			before += s[i] - '0';
		}
		cout << "Case #"<<i<<": " << out << endl;
	}



	return 0;
}