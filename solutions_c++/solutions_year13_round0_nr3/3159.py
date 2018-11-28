#include <iostream>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <algorithm>
#include <boost/multiprecision/gmp.hpp>
using namespace std;

typedef boost::multiprecision::mpz_int mint;

class Even
{
public:
    unsigned msb = 0;
    unsigned i = 0, j = 0;

    mint operator()()
    {
        if(msb == 0)
        {
            if(i == 0)
                return 11;
            else
                return 22;
        }
        else if(msb == 1)
            return 1111;

        mint bpal = 1;
        bpal = bit_set(bit_set(bit_set(bpal, i), j), msb);
    
        mint mul = 1, pal = 0;
        for(unsigned k=0; k <= msb; k++)
        {
            pal += mul*bit_test(bpal, k);
            mul *= 10;
        }
    
        for(unsigned k=0; k <= msb; k++)
        {
            pal += mul*bit_test(bpal, msb-k);
            mul *= 10;
        }

        return pal;
    }

    void next()
    {
        // Special case for 11, 22 and 1111
        if(msb == 0)
        {
            i++;
            if(i == 2)
                msb = 1;
        }
        else if(msb == 1)
        {
            msb = 2;
            i = 0;
            j = 0;
        }
        // General case
        else if(msb-1 == i && msb-2 == j)
        {
            msb++;
            i = 0;
            j = 0;
        }
        else if(i == j || i-1 == j)
        {
            i++;
            j = 0;
        }
        else
            j++;
    }
};

class Odd
{
public:
    int msb = -1;
    int i = 1, j = 0, k = 0;
    bool begWithTwo = false, endWithTwo = false;

    mint operator()()
    {
        if(msb == -1)
            return i;
        if(msb == 0)
        {
            if(i == 0)
                return 111;
            else if(i == 1)
                return 212;
            else if(i == 2)
                return 121;
        }

        mint bpal = 1;
        bpal = bit_set(bit_set(bit_set(bpal, std::max(i,0)), std::max(j,0)), std::max(k,0));

    
        mint mul = 1, pal = 0;
        for(unsigned k=0; k <= (unsigned)msb; k++)
        {
            pal += mul*bit_test(bpal, k);
            mul *= 10;
        }

        pal += mul;
        if(endWithTwo)
            pal += mul;
        mul *= 10;
    
        for(unsigned k=0; k <= (unsigned)msb; k++)
        {
            pal += mul*bit_test(bpal, msb-k);
            mul *= 10;
        }
        if(begWithTwo)
        {
            pal += 1;
            pal += mul/10;
        }
        

        return pal;
    }

    void next()
    {
        // Special case for 11, 22 and 1111
        if(msb == -1)
        {
            i++;
            if(i == 4)
            {
                msb = 0;
                i = 0;
            }
            return;
        }
        if(msb == 0)
        {
            i++;
            if(i == 3)
            {
                k = -2;
                j = -1;
                i = 0;
                msb = 1;
            }
            return;
        }
        // General case
        if(endWithTwo)
        {
            if(i == msb)
            {
                endWithTwo = false;
                msb++;
                i = 0;
            }
            else
                i++;

            return;
        }
        else if(msb == i && msb-1 == j && msb-2 == k)
        {
            endWithTwo = true;
            k = -2;
            j = -1;
            i = 0;
            return;
        }

        if(k == -2 && !begWithTwo)
        {
            begWithTwo = true;
            return;
        }
        else
            begWithTwo = false;

        k++;
        if(k == j)
        {
            k = 0;
            j++;
        }
        if(j == i)
        {
            i++;
            j = 0;
            k = -1;
        }
    }
};


std::vector<mint> fairAndSquare;

void calculateNums()
{
    Even even;
    Odd odd;

    int curMsb = odd.msb;
    bool isOdd = true;


    for(int i=0; i < 20000; i++)
    {
        mint pal;
        if(isOdd)
        {
            pal = odd();
            odd.next();

            if(curMsb != odd.msb)
            {
                isOdd = false;
                curMsb = even.msb;
            }
        }
        else
        {
            pal = even();
            even.next();

            if(curMsb != (int)even.msb)
            {
                isOdd = true;
                curMsb = odd.msb;
            }
        }

        fairAndSquare.push_back(pal*pal);
    }

    std::sort(begin(fairAndSquare), end(fairAndSquare));
}

void solve()
{
    mint A, B;
    std::cin >> A >> B;

    auto iter = begin(fairAndSquare);
    while(*iter < A) ++iter;;

    int count = 0;
    while(*iter <= B)
        count++, ++iter;

    std::cout << count;
}

int main()
{
    calculateNums();
    
	size_t n;
	std::cin >> n;
	while(std::cin.get() != '\n');
	for(size_t i=1; i <= n; i++)
	{
		std::cout << "Case #" << i << ": ";
		solve();
		std::cout << std::endl;
	}
}
