#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	
	unsigned nn;
	cin >> nn;
	for(unsigned kk=1; kk<=nn; kk++)
	{
		
		string s;
		cin >> s;
		
		unsigned res = 1;
		char prev = s[0];
		for(unsigned i=1; i<s.size(); i++)
		{
			char cur = s[i];
			if(cur != prev)
			{
				res++;
				prev = cur;
			}
		}
		
		char last = s[s.size()-1];
		if(last == '+') res--;
		
		cout << "Case #" << kk << ": " << res << endl;
		
	}
	
}
