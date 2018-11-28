#include <iostream>
#include <cstdio>
#include <string>
using namespace std;
int times;
char flat_c(char c)
{
	if(c=='+')
		return '-';
	else 
		return '+';
}
string flat(int where,string cookie)
{
	string re = "";
	for(int i = where - 1  ; i >= 0 ; i--)
	{
		re += flat_c(cookie[i]);
	}
	for(int i = where; i < cookie.size() ; i++)
	{
		re += cookie[i];
	}
	return re;
}
string flat_t(string targ,char to)
{

	//cout << targ << " to " <<to<<endl;
	if(targ.size() == 1)
	{
		if(targ[0]!=to)
		{
			targ[0] = to;
			times ++;
		}
		return targ;
	}
	else
	{
		string substring = targ.substr(0,targ.size()-1);
		string re = flat_t(substring , targ[targ.size()-1]);
		if(re[0]!=to)
		{
			times ++ ;
			re = flat(re.size(),re);
		}
		re += to;
		return re;
	}
}
int main ()
{
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	int t;
	cin >> t;
	for(int tn = 1 ;tn <= t ; tn++)
	{
		times=0;
		string cookie = "";
		cin >> cookie ;
		if(cookie.size() ==1)
		{
			if(cookie[0] == '+')
				times = 0;
			else
				times = 1;
		}
		else
		{
			string substring = cookie.substr(0,cookie.size()-1);
			string re = flat_t(substring,cookie[cookie.size()-1]);
			if(re[0]!= '+')
				times ++ ;
		}

		cout<<"Case #"<<tn<<": "<<times<<endl;

	}
	
}