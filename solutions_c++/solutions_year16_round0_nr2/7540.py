#include <iostream>
#include <fstream>
#include <string>
#include <stack>

using namespace std;

bool isAllHappy(string s)
{
	for (int i = 0; i < s.length(); i++)
	{
		if(s[i] == '-')
		{
			return false;
		}
	}
	return true;
}

string flip(string a, int pos)
{
	for (int i = 0; i < pos ; i++)
	{
		if(a[i] == '-')
		{
			a[i] = '+';
		}
		else if(a[i] == '+')
		{
			a[i] = '-';
		}
	}
	return a;
}

string putInStack(stack<char> &s, string a, int pos)
{
	for (int i = 0; i < pos; i++)
	{
		s.push(a[i]);
	}
	int j = 0;
	while (!s.empty() && j < pos)
	{
		a[j] = s.top();
		s.pop();
		j++;
	}
	return a;
}

bool isAllMinus(string a)
{
	for (int i = 0; i < a.length(); i++)
	{
		if(a[i] == '+')
		{
			return false;
		}
	}
	return true;
}

int main()
{
	ifstream in("B-large.in");
	if( !in )
	{
		cout<<"No such File exists"<<endl;
	}
	else
	{
		int T;
		in>>T;
		int  j = 0;
		ofstream out("output.txt", ios::app);
		if( T >= 0 && T <= 100 ) 
		{
			while( j < T )
			{
				string a;
				in>>a;
				stack<char> s;
				int counter = 0;
				
				while( !isAllHappy(a) )
				{
					if( !isAllMinus(a) )
					{
						int posMinus = 0, posPlus = 0;
						for( int i = 0 ; i < a.length() ; i++ )
						{
							if( a[0] == '-' )
							{
								if( a[i] == '-' )
								{
									posMinus++;
								}
								else if( a[i] == '+' )
								{
									a = putInStack(s, a, posMinus);
									a = flip(a, posMinus);
									break;
								}
							}
							else if( a[0] == '+' )
							{
								if( a[i] == '+' )
								{
									posPlus++;
								}
								else if( a[i] == '-' )
								{
									a = putInStack(s, a, posPlus);
									a = flip(a, posPlus);
									break;
								}
							}
						}
					}
					else 
					{
						counter++;
						break;
					}
					counter++;
				}
				j++;
				out<<"Case #"<<j<<": "<<counter<<endl;
			}
		}
		out.close();
	}
	in.close();
	return 0;
}
