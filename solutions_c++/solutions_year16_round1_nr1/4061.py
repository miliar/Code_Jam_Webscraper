#include <iostream>
#include <string>
#include <cstdio>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
  	freopen("A-large.out", "w", stdout);
  	int cases;
  	string s, lastword;
  	cin >> cases;
  	for (int i = 0; i < cases; i++)
  	{
  		cin >> s;
  		lastword = s[0];
  		for(int z = 1; z < s.size(); z++)
  		{
  			if(s[z] >= lastword[0])
  			{
  				lastword = s[z] + lastword;
			}
			else
			{
				lastword.push_back(s[z]);
			}
		}
		cout << "Case #" << i + 1 << ": " << lastword << endl;
	}
}
  	
