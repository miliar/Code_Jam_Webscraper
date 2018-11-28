#include<iostream>

using namespace std;

int _count(string s, bool sign)
{
	if(s.empty())
	{
		return 0;
	}
	if(s.back()=='+' && sign==true)
	{
		s.pop_back();
		return _count(s,true);
	}
	else if(s.back()=='+' && sign==false)
	{
		s.pop_back();
		return 1+_count(s,true);
	}
	else if(s.back()=='-' && sign==false)
	{
		s.pop_back();
		return _count(s,false);
	}
	else if(s.back()=='-' && sign==true)
	{
		s.pop_back();
		return 1+_count(s,false);
	}
	return 0;
}

int count(string s)
{
	if(s.empty())
	{
		return 0;
	}
	if(s.back()=='+')
	{
		s.pop_back();
		return _count(s,true);
	}
	else
	{
		s.pop_back();
		return 1+_count(s,false);
	}
}

int main()
{
	int num_cases=0;
	cin>>num_cases;
	string s;
	for(int i=0;i<num_cases;++i)
	{
		cin>>s;
		cout<<"Case #"<<i+1<<": "<<count(s)<<endl;
	}
}
