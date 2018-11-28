#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <climits>
#include <stdio.h>
#include <cmath>
#include <set>
#include <stdio.h>
#include <string.h>
#include <queue>
#include <fstream>
using namespace std;

#define INF INT_MAX / 2
#define OFFSET 11
#define NUM_ROWS 8
#define NUM_COLS 8
#define MAXN 1000 + OFFSET
#define MAXS 2500 + OFFSET
#define PRIMESCOUNT 143
#define MOD 1000000007

int main()
{
    unsigned long long in, t;
    bool digits[10] ;

    ifstream input("A-large.in");
    ofstream output("A-large.out");

    input >> t;
    //scanf("%d", &t);
    for (unsigned long long i = 1; i <= t; ++i)
    {
        input >> in;
        //scanf("%d", &in);
        unsigned long long ctr = 1, newn = in;

        memset(digits, 0, sizeof(digits));

        unsigned long long num_digits = 0, last_number;
        bool over = false;
        while(!over)
        {
            last_number = newn = ctr * in;
            if(newn == 0)
            {
                over = true;
                break;
            }
            while(newn != 0)
            {
                if ( !digits[newn % 10])
                {
                    digits[newn % 10] = 1;
                    ++num_digits;
                    if (num_digits == 10)
                    {
                        over = true;
                        break;//l
                    }
                }
                newn /= 10;
            }
            ctr++;
        }
        if (last_number == 0)
        {
            output << "Case #" << i << ": " << "INSOMNIA\n";
            //printf("INSOMNIA\n");
        } else {
            output << "Case #" << i << ": " << last_number << endl;
            //printf("Case #%d %d\n", i , last_number);
        }
    }
    output.close();
    input.close();
    return 0;
}
