#include <cstdio>
#include <vector>
#include <cmath>
#include <string>
#include <iostream>
#include <cstring>
#include <unordered_map>
#include <gmpxx.h>

using namespace std;

int const max_digits = 100; 

#if 0
int solve(int n)
{
    bool occurred[10];
    memset(occurred, 0, 10*sizeof(bool));
    //for(int i = 0; i <= 9; ++i) occurred[i] = -1;//-1 marks, never occurred

    signed char N[max_digits];
    memset(N, -1, max_digits*sizeof(signed char));
    signed char current[max_digits];
    memset(N, -1, max_digits*sizeof(signed char));
    //for(int i = 0; i <= max_digits; ++i) N[i] = -1;//-1 marks, does not exist
    
    int tmp = n;
    for(int count = 0; tmp > 0; ++count)
    {
        int last_digit = tmp%10;
        occurred[last_digit] = true;
        N[count] = last_digit;
        current[count] = last_digit;
        tmp /= 10;
    }


    while(true)
    {
        for(int i = 0; i < max_digits; ++i)
        {
            current[i] += N[i];
        }
    }

    return -1;
}
#endif

mpz_class solve2(int n)
{
    unordered_map<char, mpz_class> occurred;
    mpz_class current = n;
    char last;
    int count = 0;
    while(occurred.size() < 10 && count++ < 1000)
    {
        for(char c : current.get_str())
        {
            if(!occurred.count(c))
            {
                occurred[c] = current;
                last = c;
            }
        }
        current += n;
    }
    return occurred.size() < 10 ? mpz_class(-1) : occurred[last];
}


int main()
{
	int test_cases;
	scanf(" %d ", &test_cases);
	
    for(int i = 1; i <= test_cases; ++i)
    {
        int N;
        scanf(" %d ", &N);
        mpz_class answer = solve2(N);
        if(answer == -1)
        {
            printf("Case #%d: %s\n", i, "INSOMNIA");
        }
        else
        {
            printf("Case #%d: %s\n", i, answer.get_str().c_str());
        }
    }


	printf("\n");
	fflush(stdout);
	return 0;
}
