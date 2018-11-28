#include <string>
#include <iostream>
#include <fstream>

using namespace std;

void calc(int vals[100][100], int origin[100][100], int startX, int startY, int endX, int endY)
{
    int max = 0;
    int i = startX, j;
    do
    {
	j = startY;
	do
	{	
	    max = std::max(max, origin[i][j]);
	    ++j;
	} while (j < endY);
	++i;
    } while (i < endX);

    i = startX;
    do
    {
	j = startY;
	do
	{
	    if (vals[i][j] > max)
	    {
		vals[i][j] = max;
	    }
	    ++j;
	}
	while (j < endY);
	++i;
    } while (i < endX);
}

int main (int argc, char*argv[])
{
    ifstream input("B-large.in");
    ofstream output("out.txt");
    int x = 0;
    input >> x;
    int n, m;
    int val;
    int lawn_origin[100][100];
    int lawn[100][100];
    for (int i = 0; i < x; ++i)
    {
	input >> n >> m;
	for (int j = 0; j < n; ++j)
	{
	    for (int k = 0; k < m; ++k)
	    {
		input >> val;
		lawn_origin[j][k] = val;
		lawn[j][k] = 100;
	    }
	}
	for (int j = 0; j < n; ++j)
	{
	    calc(lawn, lawn_origin, j, 0, j, m);
	}
	for (int k = 0; k < m; ++k)
	{
	    calc(lawn, lawn_origin, 0, k, n, k);
	}
	bool result = true;
	for (int j = 0; j < n; ++j)
	{
	    for (int k = 0; k < m; ++k)
	    {
		if (lawn_origin[j][k] != lawn[j][k])
		{
		    result = false;
		    break;
		}
	    }
	    if (!result)
	    {
		break;
	    }
	}
	output << "Case #" << i + 1 << ": ";
	if (result)
	{
	    output << "YES";
	}
	else
	{
	    output << "NO";
	}
	output << std::endl;
    }
}
