#include <bits/stdc++.h>
using namespace std;
#define ll long long 

void remove(string &s,char c)
{
	for(int i=0;i<s.length();i++)
	{
		if(s.at(i)==c)
		{
			s.erase(s.begin()+i);
			return;
		}
	}
}

bool has(string s, char c)
{
	for(int i=0;i<s.length();i++)
	{
		if(s.at(i)==c)
			return true;
	}
	return false;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	int t;
	cin >> t;
	
	for(int i=1;i<=t;i++)
	{
		string s,n="";
		cin >> s;
		
			while(has(s,'Z'))
			{
				remove(s,'Z');
				remove(s,'E');
				remove(s,'R');
				remove(s,'O');
				n+="0";
			}
			while(has(s,'W'))
			{
				remove(s,'T');
				remove(s,'W');
				remove(s,'O');
				n+="2";
			}
			while(has(s,'U'))
			{
				remove(s,'F');
				remove(s,'O');
				remove(s,'U');
				remove(s,'R');
				n+="4";
			}
			while(has(s,'F'))
			{
				remove(s,'F');
				remove(s,'I');
				remove(s,'V');
				remove(s,'E');
				n+="5";
			}
			while(has(s,'X'))
			{
				remove(s,'S');
				remove(s,'I');
				remove(s,'X');
				n+="6";
			}
			while(has(s,'V'))
			{
				remove(s,'S');
				remove(s,'E');
				remove(s,'V');
				remove(s,'E');
				remove(s,'N');
				n+="7";
			}
			while(has(s,'G'))
			{
				remove(s,'E');
				remove(s,'I');
				remove(s,'G');
				remove(s,'H');
				remove(s,'T');
				n+="8";
			}
			while(has(s,'T'))
			{
				remove(s,'T');
				remove(s,'H');
				remove(s,'R');
				remove(s,'E');
				remove(s,'E');
				n+="3";
			}
			while(has(s,'O'))
			{
				remove(s,'O');
				remove(s,'N');
				remove(s,'E');
				n+="1";
			}
			while(has(s,'N'))
			{
				remove(s,'N');
				remove(s,'I');
				remove(s,'N');
				remove(s,'E');
				n+="9";
			}
		
		sort(n.begin(),n.end());
		
		cout << "Case #" << i << ": " << n << endl;
	}
}
