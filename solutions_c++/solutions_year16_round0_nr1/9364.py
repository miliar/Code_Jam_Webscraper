/*
Google CodeJam - Qualification Round
Problem A: Counting Sheep - large input
Author: Matei Iancu
*/
#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

const int MAX_ERR = 10000000;

void updateVec(int *vec, unsigned long number);
bool checkVec(int *vec);
void resetVec(int *vec);

int main()
{
	int noTests, i, j, incr, err;
    unsigned long N, num;
	int sleep[10];
	
	
	freopen("A-large.in.txt", "rt", stdin);
	freopen("A-large-output.out.txt", "wt", stdout);
	
	cin>>noTests;
	
	for(i = 0; i < noTests; i++)
	{
		cin>>N;
		
        incr = 1;
        resetVec(sleep);
        err = 0;
        
        do
        {
            num = N * incr;
            updateVec(sleep, num);
            if (checkVec(sleep))
            {
                cout<<"Case #"<<i + 1<<": "<<num<<"\n";
                break;
            }
            else
            {
                err++;
                if(err > MAX_ERR)
                {
                    cout<<"Case #"<<i + 1<<": "<<"INSOMNIA"<<"\n";
                    break;
                }
            }
            
            incr++;
        }while(true);
        
	}
	
	fclose(stdin);
	fclose(stdout);
}

void updateVec(int *vec, unsigned long number)
{
    int digit;
    do
    {
        digit = number % 10;
        vec[digit] = digit;
        
        number = number / 10;
    }while(number != 0);
}

bool checkVec(int *vec)
{
    for(int i = 0; i < 10; i++)
    {
        if(vec[i] != i)
            return false;
    }
    return true;
}

void resetVec(int *vec)
{
    for(int i = 0; i < 10; i++)
        vec[i] = -1;
}