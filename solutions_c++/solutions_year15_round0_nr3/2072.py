/*
	Michał Gańczorz
	code jam 2015
*/

#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <math.h>
#include <string>
#include <queue>
#include <list>
#include <sstream>
 // #include <unistd.h>
// #include <unordered_map>

#define ll long long

using namespace std;
const ll prime = 1000000007;

const ll big_inf =  10000000000000LL;

int arr[4][4] = 
{
  {1, 2, 3, 4},
  {2, 5, 4, 7},
  {3, 8, 5, 2},
  {4, 3, 6, 5}
};


bool poss[10033][9][9];
int pref[10033];
int suff[10033];

int toq(char c)
{
	if( c == '1')
		return 1;
	else
		return c-'i'+2;
}

int change_sing(int x)
{
	if( x > 4)
		x-=4;
	else
		x+=4;
	return x;
}

int multiply(int x1, int y1)
{
	int cs = 0;
	if(x1 > 4)
	{
		x1 -= 4;
		cs++;
	}

	if(y1 > 4)
	{
		y1 -= 4;
		cs++;
	}

	int r = 0;
	if(cs % 2)
	{
		r = arr[x1-1][y1-1];
		r = change_sing(r);
	}
	else
	{
		r = arr[x1-1][y1-1];
	}

	return r;
}

void print_char(int i)
{
	if(i > 4)
	{
		i -= 4;
		cout<<"-";	
	}

	if(i == 1)
		cout<<"1";
	else
	{
		char c = i+'i' - 2;
		cout<<c<<"\n";
	}
}

void solve(int c)
{
	int n, l;
	cin>>n>>l;
	string s, str;
	cin>>s;
	str = "";
	for(int i=0; i<l; ++i)
		str += s;

	if(str.length() < 3)
		cout<<"Case #"<<c<<": NO"<<"\n";
	else
	{
		for(int i=0; i<str.length()+2; ++i)
		{
			for(int j=1; j<=8; ++j)
			for(int k=1; k<=8; ++k)
				poss[i][j][k] = 0;
		}

		str = str + '1';
		// cout<<str<<"\n";
		poss[1][toq(str[0])][toq(str[1])] = 1;
		pref[0] = toq(str[0]);
		pref[1] = multiply(toq(str[0]), toq(str[1]));
		// poss[1][toq(str[0])][toq(str[1])] = 1;
		// cout<<toq(str[0]) <<" "<<toq(str[1])<<"\n";
		// cout<<multiply(pref[1], toq(str[2]) )<<"\n";
		// cout<<"j "<<str[2]<<"\n";
		for(int i=2; i<str.length(); ++i)
		{
			for(int j=1; j<=8; ++j)
			for(int k=1; k<=8; ++k)
			{
				if(poss[i-1][j][k] == 1)
				{
					// cout<<"I: "<<i-1<<" "<<j<<" "<<k<<"\n";

					int rr = multiply(k, toq(str[i]) );
					poss[i][j][rr] = 1;
					if(multiply(j,k) != pref[i-1])
					{
						// cout<<i<<" "<<j<<" "<<k<<"\n";
						// cout<<multiply(j,k)<<" "<<pref[i-1]<<"\n";
						// cout<<"alarm\n";
						// exit(0);
					}
				}
			}

			poss[i][pref[i-1]][toq(str[i])] = 1;
			pref[i] = multiply(pref[i-1], toq(str[i]) );
		}
		suff[str.length()-1] = toq(str[ str.length()-1]);
		suff[str.length()-2] = toq(str[ str.length()-2]);
		for(int i=str.length()-3; i>0; --i)
			suff[i] = multiply(toq(str[i]), suff[i+1]);

		// cout<<multiply(3,2)<<"\n";
		// for(int i=1; i<str.length(); ++i)
		// {
		// 	cout<<i<<" "<<suff[i]<<"\n";
		// }
		// cout<<"\n";
		// cout<<str.length()<<"\n";
		bool found = false;
		for(int i=1; i<str.length()-1; ++i)
		{
			// cout<<i<<" "<<poss[i][2][3]<<" "<<suff[i+1]<<"\n";
			if(poss[i][2][3] && suff[i+1] == 4)
				found = true;
		}
		// cout<<"\n";

		if(found)
			cout<<"Case #"<<c<<": YES"<<"\n";
		else
			cout<<"Case #"<<c<<": NO"<<"\n";

		// cout<<pref[1]<<"\n";
		// print_char(pref[3]);
		// cout<<"\n";
	}
}

int main()
{
	// ios_base::sync_with_stdio(0);
	// cin.tie(NULL);

	int t;
	cin>>t;
	for(int i=1; i<=t; i++)
		solve(i);

	return 0;
}