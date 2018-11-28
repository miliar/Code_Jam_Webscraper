#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

// 1 = 1 ; 2 = i ; 3 = j ; 4 = k

int toNum(char c)
{
    switch(c)
    {
        case 'i' : return 2;
        case 'j' : return 3;
        case 'k' : return 4;
    }

    return 1;
}

int product(int a, int b)
{
    int sign = a*b;

    if(a < 0)
        a = -a;
    if(b < 0)
        b = -b;

    static int tab[4][4] = {{1, 2, 3, 4}, {2, -1, 4, -3}, {3, -4, -1, 2}, {4, 3, -2, -1}};

    return (sign > 0) ? tab[a-1][b-1] : -tab[a-1][b-1];
}

bool find(int L, int K, string str)
{
    const int i = 2, ij = product(i, 3), ijk = product(ij, 4);

    // Does the chain equals to ijk ?

    long int prodOne = 1, prodTot = 1;

    for(int x = 0 ; x < L ; x++)
        prodOne = product(prodOne, toNum(str[x]));

    for(int x = 0 ; x < K % 4 ; x++)
        prodTot = product(prodTot, prodOne);

    if(prodTot != ijk)
        return false;

    // Find the initial 'i'

    long int max = (L*K > 8*L) ? 8*L : L*K;
    int currProd = 1;
    long int x = 0;

    for(x = 0 ; x < max ; x++)
    {
        currProd = product(currProd, toNum(str[x % L]));

        if(currProd == i)
        {
            x++;
            break;
        }
    }

    if(currProd != i)
        return false;

    for(; x < max ; x++)
    {
        currProd = product(currProd, toNum(str[x % L]));

        if(currProd == ij)
            return true;
    }

    return false;
}

int main()
{
    ifstream input("input.txt");
    ofstream output("output.txt");

    int nbTests = 0, L, K;
    string str;

    input >> nbTests;

    for(int i = 0 ; i < nbTests ; i++)
    {
        input >> L >> K >> str;

        if(find(L, K, str))
            output << "Case #" << i+1 << ": YES" << endl;
        else
            output << "Case #" << i+1 << ": NO" << endl;

    }

    input.close();
    output.close();

    return 0;
}
