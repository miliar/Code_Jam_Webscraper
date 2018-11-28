#include <iostream>
using namespace std;

int main()
{
	int T,res=0;
	cin >> T;
	for(int t=1;t<=T;t++)
	{
		res=0;
		string s;
		cin >> s;
		for(int i=1;i<s.size();i++)
			if(s[i]!=s[i-1])
				res++;
		res+=s[s.size()-1]=='-';
		cout << "Case #" << t << ": " << res << endl;
	}
	return 0;
}
