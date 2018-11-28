/*
 ID: Joe Montano
 PROG: pprime
 LANG: C++
 */

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdlib>
#include <cmath>

using namespace std;

bool isPal(string input)
{
	for(int i=0; i<=input.length()/2; i++)
	{
		if(input[i] != input[(input.length()-1)-i])
		{
			return false;
		}
	}
	return true;
}

int main()
{
	//freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);

	int trials,a,b;
	cin >> trials;

	int runs = 1;

	while (runs <= trials)
	{
		cin >> a >> b;
		int count = 0;
		for(int i=0; i<=10000000; i++)
		{
			int square = i*i;
			stringstream s;
			stringstream x;
			x << i;
			s << square;
			if(square > b)
			{
				break;
			}
			if(isPal(s.str()) && isPal(x.str()) && square >=a && square <=b)
			{
				count ++;
				//cout << s.str() << " " ;
			}
		}

		//cout << a << " " << b << endl;
		cout << "Case #" << runs << ": " << count << endl;
		runs++;
	}
	return 0;
}