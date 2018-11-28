#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
using namespace std;

#define PI M_PI

double dist(int x, int y)
{
  return sqrt(x*x+y*y);
}

bool is_pal(long val);

int main()
{
	ifstream input;
	string line;
	char *tstr;
	int T;
	
	long A, B;
	long ans;
	
	long i, j;
	
    long start, end;

	//input.open("sample.in");
	//input.open("C-small-attempt0.in");
	input.open("C-large-1.in");
	//input.open("");

	getline(input, line);

	T = atoi(line.c_str()); /* 1 <= T <= 10000 */

	for(int run=1; run<=T; run++)
	{
		ans = 0;
        
		input >> A;
		input >> B;

        start = ceil(sqrt(A));
        end   = floor(sqrt(B));
        
        for(i=start; i<=end; i++)
        {
			if(is_pal(i) && is_pal(i*i))
			{
				ans++;
			}
		}
		
		cout << "Case #" << run << ": " << ans << endl;
	}
	
	return 0;
}

bool is_pal(long val)
{
	char valstr[15];
	int  size;
	
	size = 0;
	while(val>0)
	{
		valstr[size] = val%10 + 48;
		val/=10;
		size++;
	}

	for(int i=0; i<size/2; i++)
	{
		if(valstr[i] != valstr[size-i-1])
		{
			return false;
		}
	}
	
	return true;
}
