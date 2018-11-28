#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
#include <iomanip>

using namespace std;

#define LL long long

#define FOR(i,a,b) for(int i = a ; i < b ; i++)
#define FORI(i,b,a) for(int i = b ; i >= a ; i--)

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin >> T;
	FOR(tc,1,T+1)
	{
		string str;
		cin >> str;
		map <char, int> numToCount;
		FOR(i,0,str.size())
		{
			numToCount[str[i]]++;
		}
		string ans = "";
		while(numToCount['X'] > 0)
		{
			ans = ans + '6';
			numToCount['S']--;
			numToCount['I']--;
			numToCount['X']--;	
		}
		while(numToCount['W'] > 0)
		{
			ans = ans + '2';
			numToCount['T']--;
			numToCount['W']--;
			numToCount['O']--;	
		}
		while(numToCount['U'] > 0)
		{
			ans = ans + '4';
			numToCount['F']--;
			numToCount['O']--;
			numToCount['U']--;	
			numToCount['R']--;
		}
		while(numToCount['Z'] > 0)
		{
			ans = ans + '0';
			numToCount['Z']--;
			numToCount['E']--;
			numToCount['R']--;	
			numToCount['O']--;	
		}
		while(numToCount['G'] > 0)
		{
			ans = ans + '8';
			numToCount['E']--;
			numToCount['I']--;
			numToCount['G']--;	
			numToCount['H']--;	
			numToCount['T']--;	
		}
		while(numToCount['H'] > 0)
		{
			ans = ans + '3';
			numToCount['T']--;
			numToCount['H']--;
			numToCount['R']--;	
			numToCount['E']--;	
			numToCount['E']--;
		}
		while(numToCount['F'] > 0)
		{
			ans = ans + '5';
			numToCount['F']--;
			numToCount['I']--;
			numToCount['V']--;	
			numToCount['E']--;
		}
		while(numToCount['V'] > 0)
		{
			ans = ans + '7';
			numToCount['S']--;
			numToCount['E']--;
			numToCount['V']--;	
			numToCount['E']--;	
			numToCount['N']--;
		}
		while(numToCount['I'] > 0)
		{
			ans = ans + '9';
			numToCount['N']--;
			numToCount['I']--;
			numToCount['N']--;	
			numToCount['E']--;
		}
		while(numToCount['O'] > 0)
		{
			ans = ans + '1';
			numToCount['O']--;
			numToCount['N']--;
			numToCount['E']--;
		}
		sort(ans.begin(), ans.end());
		cout << "Case #" << tc << ": " << ans << endl;
	}
	return 0;
}
