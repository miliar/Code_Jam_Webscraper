#include <bits/stdc++.h>

using namespace std;

int test()
{
	string s;
	cin>>s;
	while(s.size() > 0 && s.back() == '+')
		s.pop_back();
	if (s.size() == 0)
		return 0;
	int wyn = 1;
	for(int i=1; i<s.size(); i++)
		if (s[i] != s[i-1])
			wyn++;
	return wyn;
}

int main()
{
	int testy;
	cin>>testy;
	for(int i=1; i<=testy; i++)
	{
		cout << "Case #"<<i<<": "<<test()<<"\n";
	}
}
