#include <iostream>
#include <string>
#include <algorithm>
#include <iomanip>
#include <cstdio>
#include <set>
#include <cstdlib>
#include <ctime>
#include <sstream>
#include <vector>
#include <string.h>
using namespace std;
#define NN 100000
#define ll long long
#define pii pair<int,int>

bool vowel(char c)
{
	if(c == 'a' || 
	   c == 'e' || 
	   c == 'i' || 
	   c == 'o' ||
	   c == 'u')
	   return false;
	return true;
}

int main()
{
	ll t;
	ll n;
	string s;
	
	cin >> t;
	ll res;
	int now;
	for(ll cas = 1; cas <= t; cas ++)
	{
		cin >> s >> n;
		res = 0;
		int i = 0;
		int j = 0;
		int k = n-1;
		now = 0;
		for(int h = 0; h <= k; h ++)
			now += vowel( s[h] );
		while(k < s.size())
		{
			if(now >= n)
			{
				while(i <= j)
				{
					res += s.size()-k;
					i ++;
				}
				if( vowel(s[j]) == true )
					now --;
				j ++;
				k ++;
				if( vowel(s[k]) == true )
					now ++;
			}
			else
			{
				if( vowel(s[j]) == true )
					now --;
				j ++;
				k ++;
				if( vowel(s[k]) == true )
					now ++;
			}
		}		
		cout << "Case #" << cas << ": " << res << endl;
	}
	
	return 0;
}