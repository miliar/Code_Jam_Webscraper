#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <stack>
using namespace std; 

typedef stack<bool> SB;

const int PLUS = 0;
const int MINUS = 1;
const int NEUTRAL = 3;

int k, c, s;
SB happy;

void read(char sign)
{
	std::string line;
	std::getline(cin, line);
	std::istringstream iss(line);
	while(iss >> sign)
	{
		if(sign == '+') s = PLUS;
		else
		{
			if(s == PLUS) ++k;
			if(s != MINUS) ++k;
			s = MINUS;
		};
	}
}

int main()
{
	int m;
	cin >> m;
	for(c = 1; c <= m; ++c)
	{
		s = NEUTRAL;
		k = 0;
		char sign = '.';
		if(c==1) read(sign);
		read(sign);
		cout << "Case #" << c << ": " << k <<endl;
	}
}
