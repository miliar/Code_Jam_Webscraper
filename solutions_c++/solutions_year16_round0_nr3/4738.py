#include <iostream>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <algorithm>
#include <fstream>
using namespace std;

typedef unsigned __int128 ui;

//constexpr size_t N = 6;
//constexpr size_t J = 3;
//constexpr size_t N = 16;
//constexpr size_t J = 50;
constexpr size_t N = 32;
constexpr size_t J = 500;

istream& operator>>(istream& in, ui& n)
{
    unsigned nn; in >> nn;
    n = nn;
    return in;
}

ostream& operator<<(ostream& out, ui n)
{
    std::string nn;
    while(n != 0)
    {
        nn.insert(begin(nn), (n%10) + '0');
        n /= 10;
    }

    out << nn;
    return out;
}

class Solve
{
public:
    ui multiples[11][N];
    vector<ui> primeNumbers;

    void computePrimes()
    {
        primeNumbers.push_back(2);

        for (ui n = 3; n < 100; n += 2)
        {
            for (auto p : primeNumbers)
            {
                if (n % p == 0)
                    goto nonprime;
            }
            primeNumbers.push_back(n);
        nonprime:;
        } 
    }

    void writePrimes()
    {
        ofstream out("primes");
        for (auto p : primeNumbers)
            out << p << " ";
    }

    void readPrimes()
    {
        ifstream in("primes");
        while(in)
        {
            ui p; in >> p;
            if (in)
                primeNumbers.push_back(p);
        }
    }

    void check()
    {
        ui n, j;
        std::cin >> n >> j;
        if (n != N || j != J)
        {
            std::cout << "Wrong input!" << std::endl;
            exit(0);
        }
    }
    
    void solve()
    {
        check();

        // Compute a list of multiples
        for (size_t i = 2; i <= 10; ++i)
        {
            ui m = 1;
            for (size_t j = 0; j < N; ++j, m *= i)
            {
                multiples[i][j] = m;
            }
        }

        //computePrimes();
        //writePrimes();
        readPrimes();

        ui l = 1|(1<<(N-1));
        for(size_t found = 0; found < J; l += 2)
        {
            ui lr[11];
            for (size_t i = 2; i <= 10; ++i)
            {
                lr[i] = 0;
                for (size_t j = 0; j < N; ++j)
                    if(l & (1<<j))
                        lr[i] += multiples[i][j];
            }

            ui divisors[11];
            size_t divisorsFound = 0;
            for (size_t i = 2; i <= 10; ++i)
                divisors[i] = 0;
            for (auto p : primeNumbers)
            {
                for (size_t i = 2; i <= 10; ++i)
                {
                    if(divisors[i] == 0 && lr[i] % p == 0)
                    {
                        ++divisorsFound;
                        divisors[i] = p;

                        if (divisorsFound == 9)
                        {
                            std::cout << lr[10];
                            for (size_t j = 2; j <= 10; ++j)
                                std::cout << " " << divisors[j];
                            std::cout << std::endl;
                            ++found;
                            goto next;
                        }
                    }
                }
            }

        next:;
        }
    }
};

int main()
{
	size_t n;
	std::cin >> n;
	while(std::cin.get() != '\n');
	for(size_t i=1; i <= n; i++)
	{
		std::cout << "Case #" << i << ": " << std::endl;
        Solve s;
		s.solve();
		std::cout << std::endl;
	}
}
