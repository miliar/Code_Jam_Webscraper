#include <iostream>
#include <string>
#include <sstream>
#include <set>
#include <algorithm>

using namespace std;

int main()
{
	set<int> cmpVec;
	for(int i=0; i<10; ++i)
		cmpVec.insert(i);
	int n=0;
	cin>>n;
	
	for(int i=0; i<n; ++i)
	{
		set<int> digits;
		unsigned long long num;
		unsigned long long result;
		cin>>num;
		if(num==0)
		{
			cout<<"Case #"<<i+1<<": INSOMNIA"<<"\n";
			continue;
		}
		int t=0;
		while(digits.size()!=cmpVec.size())
		{
			++t;
			unsigned long long newnum=num*t;
			result = newnum;
			
			string s;
			stringstream ss(s);
			ss << newnum;
			s=ss.str();
			for(int j=0; j<s.length(); ++j)
			{
				int digit = s[j]-'0';
				digits.insert(digit);
			}
		}
		cout<<"Case #"<<i+1<<": "<<result<<"\n";
		
	}
	return 0;
}