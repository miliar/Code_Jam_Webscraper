#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <sstream>
using namespace std;

#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)
typedef long long ll;
string dig[]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
string dig1[]={"THREE", "NINE"};
int main(int argc, char const *argv[])
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int tt, tn, pos; cin >> tn;

	F1(tt,tn) {
		string d;
		cin>>d;
		string ans="";
		while(d!="")//0
		{
			if((pos=d.find('Z'))!=string::npos)
			{
				d.erase(pos,1);
				d.erase(d.find('E'),1);
				d.erase(d.find('R'),1);
				d.erase(d.find('O'),1);
				ans+="0";
			}
			else
				break;
		}
		while(d!="")//2
		{
			if((pos=d.find('W'))!=string::npos)
			{
				d.erase(pos,1);
				d.erase(d.find('T'),1);
				// d.erase(d.find('R'),1);
				d.erase(d.find('O'),1);
				ans+="2";
			}
			else
				break;
		}
		while(d!="")//4
		{
			if((pos=d.find('U'))!=string::npos)
			{
				d.erase(pos,1);
				d.erase(d.find('F'),1);
				d.erase(d.find('R'),1);
				d.erase(d.find('O'),1);
				ans+="4";
			}
			else
				break;
		}
		while(d!="")//6
		{
			if((pos=d.find('X'))!=string::npos)
			{
				d.erase(pos,1);
				d.erase(d.find('S'),1);
				d.erase(d.find('I'),1);
				// d.erase(d.find('O'),1);
				ans+="6";
			}
			else
				break;
		}
		while(d!="")//8
		{
			if((pos=d.find('G'))!=string::npos)
			{
				d.erase(pos,1);
				d.erase(d.find('E'),1);
				d.erase(d.find('I'),1);
				d.erase(d.find('H'),1);
				d.erase(d.find('T'),1);
				ans+="8";
			}
			else
				break;
		}
		while(d!="")//1
		{
			if((pos=d.find('O'))!=string::npos)
			{
				d.erase(pos,1);
				d.erase(d.find('N'),1);
				d.erase(d.find('E'),1);
				// d.erase(d.find('H'),1);
				// d.erase(d.find('T'),1);
				ans+="1";
			}
			else
				break;
		}
		while(d!="")//5
		{
			if((pos=d.find('F'))!=string::npos)
			{
				d.erase(pos,1);
				d.erase(d.find('I'),1);
				d.erase(d.find('E'),1);
				d.erase(d.find('V'),1);
				// d.erase(d.find('T'),1);
				ans+="5";
			}
			else
				break;
		}
		while(d!="")//7
		{
			if((pos=d.find('S'))!=string::npos)
			{
				d.erase(pos,1);
				d.erase(d.find('E'),1);
				d.erase(d.find('V'),1);
				d.erase(d.find('E'),1);
				d.erase(d.find('N'),1);
				ans+="7";
			}
			else
				break;
		}
		while(d!="")//3
		{
			if((pos=d.find('T'))!=string::npos)
			{
				d.erase(pos,1);
				d.erase(d.find('H'),1);
				d.erase(d.find('R'),1);
				d.erase(d.find('E'),1);
				d.erase(d.find('E'),1);
				ans+="3";
			}
			else
				break;
		}
		while(d!="")//9
		{
			if((pos=d.find('N'))!=string::npos)
			{
				d.erase(pos,1);
				d.erase(d.find('I'),1);
				d.erase(d.find('N'),1);
				d.erase(d.find('E'),1);
				// d.erase(d.find('E'),1);
				ans+="9";
			}
			else
				break;
		}
		sort(ans.begin(),ans.end());
		printf("Case #%d: ", tt);
		cout << ans << endl;
	}

	return 0;
}