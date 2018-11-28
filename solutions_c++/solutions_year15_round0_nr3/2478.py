#include <iostream>
#include <string>

using namespace std;

enum Letter
{
    one = 1,
    i = 2,
    j = 3,
    k = 4
};

int multiply(int a, int b)
{
    int sign = a*b;
    if (sign < 0)
    {
	sign = -1;
    }
    else
    {
	sign = 1;
    }
    if (a < 0)
    {
	a *= -1;
    }
    if (b < 0)
    {
	b *= -1;
    }
    int retval = 0;
    if (a == one)
    {
	retval = b;
    }
    if (b == one)
    {
	retval = a;
    }
    if (a == b)
    {
	retval = -1;
    }
    if (a == i)
    {
	if (b == j)
	{
	    retval = k;
	}
	if (b == k)
	{
	    retval = -j;
	}
    }
    if (a == j)
    {
	if (b == i)
	{
	    retval = -k;
	}
	if (b == k)
	{
	    retval = i;
	}
    }
    if (a == k)
    {
	if (b == i)
	{
	    retval = j;
	}
	if (b == j)
	{
	    retval = -i;
	}
    }
    return retval * sign;
}

int convert(char c)
{
    if (c == 'i')
    {
	return i;
    }
    else if (c == 'j')
    {
	return j;
    }
    else if (c == 'k')
    {
	return k;
    }
}

int reduce(string line, int start, int finish)
{
    int current = convert(line[start]);
    for (int index = start + 1; index < finish; index++)
    {	
	current = multiply(current, convert(line[index]));
    }
    return current;
}

/*void print(string line, int s, int f)
{
    for (int index = s; index < f; index++)
    {
	cout << line[index];
    }
    cout << endl;
    }*/

/*bool partition(string line)
{
    for (int x = 0; x < line.size(); x++)
    {
	if (reduce(line, 0, x) == i)
	{
	    for (int y = x+1; y < line.size(); y++)
	    {
		if (reduce(line, x, y) == j
		    && reduce(line, y, line.size()) == k)
		{
		    print(line, 0, x);
		    print(line, x, y);
		    print(line, y, line.size());
		    return true;
		}
	    }
	}
    }
    return false;
    }*/

bool findk(string line, int start, int finish)
{
    int current = convert(line[start]);
    int index;
    for (index = start + 1; index < finish; index++)
    {
	current = multiply(current, convert(line[index]));
    }
    if (current == k)
    {
	//print(line, start, index);
	return true;
    }
    return false;
}

bool findj(string line, int start, int finish)
{
    int current = convert(line[start]);
    for (int index = start + 1; index < finish; index++)
    {
	if (current == j)
	{
	    //print(line, start, index);
	    return findk(line, index, finish);
	}
	current = multiply(current, convert(line[index]));
    }
    return false;
}

bool findi(string line, int start, int finish)
{
    int current = convert(line[start]);
    for (int index = start + 1; index < finish; index++)
    {
	if (current == i)
	{
	    //print(line, start, index);
	    return findj(line, index, finish);
	}
	current = multiply(current, convert(line[index]));
    }
    return false;
}

int main()
{
    int numCases;
    cin >> numCases;
    for (int c = 1; c <= numCases; c++)
    {
	int L, X;
	cin >> L;
	cin >> X;
	string word;
	cin >> word;
	string line = "";
	for (int i = 0; i < X; i++)
	{
	    line += word;
	}
	//cout << "Line: " << line << endl;
	if (findi(line, 0, L*X))
	{
	    cout << "Case #" << c << ": YES" << endl;
	}
	else
	{
	    cout << "Case #" << c << ": NO" << endl;
	}
    }
}
