#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

string input(string old,char c)
{
	if(old == "")
	{
		string newc(1,c);
		return newc;
	}
	else
	{
		string newc(1,c);
		if(old[0] - c <= 0)
			return newc + old;
		else
			return old + newc;

	}

}
int main ()
{
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	int t;
	cin >> t;
	for(int tn = 1 ; tn <= t ; tn ++)
	{
		string s;
		cin >> s;
		string con = "";
		int n = 0;
		while (n < s.length())
		{
			con = input(con,s[n]);
			n++;
		}
		cout<<"Case #" << tn  <<": "<<con<<endl;
	}
}