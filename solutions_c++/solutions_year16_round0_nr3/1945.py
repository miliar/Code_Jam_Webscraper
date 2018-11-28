#include <iostream>
#include <fstream>
#include <string>
#include "bigint/BigIntegerLibrary.hh"

void plusOne(std::string& s)
{
    for(int i(1); i <= s.size(); i++)
    {
        if(s[s.size()-i] == '0')
        {
            s[s.size()-i] = '1';
            break;
        }
        else
        {
            s[s.size()-i] = '0';
        }
    }
}

BigUnsigned isPrime(BigUnsigned x)
{
    for(BigUnsigned i(2); i < (x/i) && i < BigUnsigned(10000); i++)
    {
        if(x%i == 0)
        {
            return i;
        }
    }
    return 0;
}

BigUnsigned pow(BigUnsigned x, BigUnsigned p)
{
    if(p == 0)
        return 1;
    else
        return x*pow(x, p-1);
}

BigUnsigned toBase(const std::string& s, BigUnsigned base)
{
    BigUnsigned b(BigUnsigned(1)+pow(base, s.size()+1));
    for(BigUnsigned i(1); i <= s.size(); i++)
    {
        b += BigUnsigned(s[s.size()-i.toInt()]-'0')*pow(base, i);
    }
    return b;
}

std::string isCoin(const std::string& s)
{
    std::string tmp("1");
    tmp += s;
    tmp += "1";
    for(BigUnsigned base(2); base < 11; base++)
    {
        BigUnsigned b = toBase(s, base);
        BigUnsigned f = isPrime(b);

        //std::cout << "base : " << base << " ; " << b << " ; " << isPrime(b) << std::endl;

        if(f == 0)
        {
            return "";
        }
        else
        {
            tmp += " ";
            tmp += bigIntegerToString(f);
        }
    }
    return tmp;
}

int main()
{
    std::cout << toBase("00000000000000",8) << " " << isPrime(toBase("00000000000000",8)) << std::endl;

    std::ifstream in("in");
    std::ofstream o("out");

    int nb(0);
    in >> nb;

    for(int i(0); i < nb; i++)
    {
        o << "Case #" << i+1 << ":" << std::endl;

        int taille(0);
        in >> taille;

        int n(0);
        in >> n;

        std::string s(taille-2, '0');

        for(int j(0); j < n;)
        {
            std::string tmp(isCoin(s));
            if(tmp.size() > 0)
            {
                o << tmp << std::endl;
                std::cout << tmp << std::endl;
                j++;
            }
            plusOne(s);
        }
    }

    return 0;
}
