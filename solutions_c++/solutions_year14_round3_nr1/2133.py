#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <math.h>
#include <cmath>

#define FORI(a,b) for(unsigned int i=(a); i < (b); i++)
#define FORJ(a,b) for(unsigned int j=(a); j < (b); j++)
#define FORK(a,b) for(unsigned int k=(a); k < (b); k++)

using namespace std;

double Log2( double n )  
{  
    // log(n)/log(2) is log2.  
    return log( n ) / log( 2 );  
}

unsigned int isEven(unsigned int top, unsigned int bot, unsigned int depth)
{
	unsigned int check;
	if (depth > 40)
		return 0;
	if (bot == top)
		return depth;
	else if (bot < top)
	{
		check = isEven(top - bot, bot, 0);
		if (!check)
			return 0;
		else
			return depth;
	}
	else if (bot & 0x01)
		return 0;
	else
		return isEven(top, bot/2, depth+1);
}

int main()
{
	unsigned int T;
	unsigned int len;
	unsigned int temp;
	double gencalc;
	string el;
	string top, bot;
	string * str;
	cin >> T;

	for (unsigned int c=1; c <= T; c++)
	{
		el.clear();
		cin >> el;
		temp = 0;
		gencalc = 0;
		len = el.size();
		top.clear();
		bot.clear();

		str = &top;
		

		while (temp < len)
		{
			if (el[temp] == '/')
			{
				str = &bot;
			}
			else
			{
				(*str).push_back(el[temp]);
			}
			temp++;
		}
		temp = isEven(stoul(top), stoul(bot), 0);
		if (!temp)
		{
			cout << "Case #" << c << ": " << "impossible" << endl;
		}
		else
		{
			cout << "Case #" << c << ": " << temp << endl;
		}
	}
	return 0;
}
