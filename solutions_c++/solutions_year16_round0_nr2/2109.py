#include <iostream>
#include <algorithm>
#include <map>
int answer[200][200][2][2];

bool match(char c, bool fl)
{
	if (fl)
	{
		return c == '+';
	}
	else
	{
		return c == '-';
	}
}
std::map<std::string, int> cache[2]; 
int f(std::string string, bool fl)
{
	if (string.size() == 1)
	{
		return !match(string[0], fl);
	}
	if (match(string[0], fl))
	{
		return f(string.substr(1), fl);
	}
	if (cache[fl].count(string))
	{
		return cache[fl][string];
	}
	int best = 1 << 30;
	for (int i = 1; i < string.size(); ++i)
	{
		std::string left = string.substr(0, i);
		std::string right = string.substr(i);
		std::reverse(left.begin(), left.end());
		int val = f(left, !fl) + 1 + f(right, !fl);
	        best = std::min(val, best);	
	}
	cache[fl][string] = best;
	return best;
}
int main()
{
    int testNum;
    std::cin >> testNum;
    for(int testId = 1; testId <= testNum; testId++)
    {
	std::string string;
	std::cout << "Case #" << testId << ": ";
	memset(answer, -1 ,sizeof(answer));
	std::cin >> string;
	std::reverse(string.begin(), string.end());
	std::cout << f(string, true) << std::endl;

    }
    return 0;
}

