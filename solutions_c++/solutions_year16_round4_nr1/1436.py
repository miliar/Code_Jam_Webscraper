#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <iomanip>
#include <queue>

using namespace std;

map<char, char> movelocs;

string dfs_from(char s, int levels)
{
	string ns = "";
	if(levels == 0)
	{
		ns = " ";
		ns[0] = s;
		return ns;
	}
	string a = dfs_from(s, levels-1);
	string b = dfs_from(movelocs[s], levels-1);
	ns += min(a, b);
	ns += max(a, b);
	return ns;
}

int main()
{
	movelocs['R'] = 'S';
movelocs['P'] = 'R';
movelocs['S'] = 'P';
  int n;
  cin >> n;
  for(int i = 1; i <= n; i++)
  {
    //solving
  	long long pow, r, p, s;
  	cin >> pow >> r >> p >> s;
  	long long a=1,b=0,c=0, temp;

  	for(int j = 0; j < pow; j++)
  	{
  		temp = a;
  		a += b;
  		b += c;
  		c += temp;
  	}

  	//make a matching
  	//rps
  	//psr
  	//spr
	  string move = "RPS";
 
  	string possibles = "Z";
  	int order = 3;
		if(a == s && b == r && c == p)
		{
	  	order = 1;
			
	  	possibles = min(possibles, dfs_from('S', pow));
		}
		if(a == r && b == p && c == s)
		{
			order = 1;
			
	  	possibles = min(possibles, dfs_from('R', pow));
		}
		if(a == p && b == s && c == r)
		{
			order = 1;
			
	  	possibles = min(possibles, dfs_from('P', pow));
		}
    
    cout << "Case #" << i << ": ";
    //output
    if(order == 3)
    	cout << "IMPOSSIBLE" << endl;
    else
    {
    	cout << possibles << endl;
    }
  }
  return 0;
}
