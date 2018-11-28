// GoogleCodeJam2014Cplusplus.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <vector>
#include <math.h>
#include <algorithm>

using namespace std;



string binary(int a)
{
    string bbinary = "";
    int mask = 1;
    for(int i = 0; i < 31; i++)
    {
        if((mask&a) >= 1)
            bbinary = "1"+bbinary;
        else
            bbinary = "0"+bbinary;
        mask<<=1;
    }
    return bbinary;
}

unsigned binary_to_decimal(unsigned num)
{
    unsigned res = 0;

    for(int i = 0; num > 0; ++i)
    {
        if((num % 10) == 1)
            res += (1 << i);

        num /= 10;
    }

    return res;
}

string AND(string first, string second)
{
	string res = "";
	
	if(second.size() > first.size())
		swap(first, second);

	for(int i = 0; i < second.size(); i++ )
	{
		if(first[i] == '1' && second[i] == '1')
			res = "1" + res;
		else
			res = "0" + res;
	}

	for(int i = 0; i < first.size() - second.size(); i++ )
	{
		res = "0" + res;
	}
	return res;
}

int main()
{

    ifstream input("A-small-attempt0.in");
    ofstream output("Output.txt");

	 int tasks;

	input >> tasks;

	long int p, q;
	long int q1;
	long unsigned int p1;

	
	int count;
	bool possible;
	char temp;
	
	for(int i = 1; i <= tasks; i++)
	{
		input >> p >> temp >> q;

		int j = 0;
		count = 0;
		possible = false;

		while(p < q && j < 40)
		{
			p *= 2;
			j++;
		}

		q1 = q;
		p1 = p - q;
		count = j;

		for(j ; j < 40; j++)
		{
			if(( p1 = (p1 % q1)) == 0)
			{
				possible = true;
				break;
			}

			p1 *= 2;
		}
		

			
		if(possible)
			output << "Case #"<<i<<": "<< count <<"\n";
		else
			output << "Case #"<<i<<": "<< "impossible" <<"\n";
	}
    

    input.close();
    output.close();
	return 0;
}



