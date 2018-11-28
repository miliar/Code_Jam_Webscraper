#include <stdlib.h>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include "CountingSheep.h"

using namespace std;

bool digits [10];
int numDigits = 0;

CountingSheep::CountingSheep()
{
}

string CountingSheep::countSheep(string input)
{
    reset();
    int base;
    int number = 0;
    int sheepCounted = 0;
    bool done = false;

    base = strtol(input.c_str(), NULL, 10);
    if(base == 0)
    {
        return "INSOMNIA";
    }

    while(!done && sheepCounted < 100)
    {
        number += base;
        done = checkDigits(number);
        sheepCounted++;
    }
    return intToString(number);
}

bool CountingSheep::checkDigits(int number)
{
    while(number)
    {
        if(!digits[number % 10])
        {
            digits[number % 10] = true;
            numDigits++;
        }
        number /= 10;
    }

    return numDigits == 10;
}

string CountingSheep::intToString(int number)
{
    stringstream ss;
	ss << number;
	return ss.str();
}

void CountingSheep::reset()
{
    for(bool &b : digits)
    {
        b = false;
    }
    numDigits = 0;
}
