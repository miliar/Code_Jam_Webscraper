#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<sstream>
#include<math.h>
using namespace std;
bool check_palindrome(long long j)
{
	string s;
	ostringstream c;
	c << j;
	s = c.str();
	for(int k=0;k<s.size();k++)
	{
		if(s[k]!=s[s.size()-k-1])
		{
			return false;
		}
	}
	return true;
}
int main()
{
	ifstream cin;
	ofstream cout;
	cin.open("C-large-1.in");
	cout.open("outputprob3large.txt");
	int t;
	long long a,b;
	cin>>t;
	a = 1;
	b = 100000000000000;
	vector<long long> val;
	long long temp = 1;
	long long temp2 = temp*temp;
	bool nice;
	while(temp2<=b)
	{
		nice = check_palindrome(temp);
		if(nice)
		{
			nice = check_palindrome(temp2);
		}
		if(nice)
		{
			val.push_back(temp2);
		}
		temp++;
		temp2 =temp*temp;
	}
	for(int i=0;i<t;i++)
	{
		long counter = 0;
		cin>>a>>b;
		for(int k=0;k<val.size();k++)
		{
			if(a<=val[k] && b>=val[k]) counter++;
		}
		cout<<"Case #"<<i+1<<": "<<counter<<endl;
	}
	return 0;
}
