#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
#include <stack>
using namespace std;

bool isSorted(stack<char> s)
{
	while(!s.empty())
	{
		if(s.top()!='+')
			return 0;
		s.pop();			
	}
	return 1;
}
int main()
{
	stack<char> s, t_s;
	long long int T;
	cin>>T;
	int t=1;
	while(t<=T)
	{
		string str;
		cin>>str;
		long long int i=0;
		while(str[i]!='\0')
		{
			t_s.push(str[i]);	
			i++;
		}
		while(!t_s.empty())
		{
			s.push(t_s.top());
			t_s.pop();		
		}
		char ch=s.top();
		char c_ch;
		long long int m=0;
		while(!isSorted(s))
		{
			if(ch=='+')
			{
				c_ch='-';
			}
			else
			{
				c_ch='+';
			}
			while(!s.empty()&&s.top()==ch)
			{
				t_s.push(c_ch);
				s.pop();
			}
			while(!t_s.empty())
			{
				s.push(t_s.top());
				t_s.pop();
			}
			ch=c_ch;
			m++;
		}
		cout<<"Case #"<<t<<":"<<" "<<m<<"\n";
		t++;		
	}
}
