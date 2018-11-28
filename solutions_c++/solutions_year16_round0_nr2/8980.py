#include <iostream>
#include <string>
#include <sstream>
#include <set>
#include <algorithm>

using namespace std;

int main()
{
	int n=0;
	cin>>n;
	
	for(int i=0; i<n; ++i)
	{
		string s;
		cin>>s;
		char last = '0';
		int times = 0;
		for(int j=0; j<s.length(); ++j)
		{
			last = s[j];
			if((j+1)<s.length())
				if(last!=s[j+1])
					++times;
		}
		if(last=='-')
			++times;
		
		cout<<"Case #"<<i+1<<": "<<times<<"\n";
		
	}
	return 0;
}