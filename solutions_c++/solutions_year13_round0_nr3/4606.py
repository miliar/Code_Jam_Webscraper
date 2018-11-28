#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORI(i,b) FOR(i,0,b)

bool palindrome(unsigned long long int i)
{
    unsigned long long int j=0;
    unsigned long long int k=i;
    while(k!=0)
    {
        j*= 10;
        j+= k%10;
        k/= 10;
    }
    if(j==i) return true;
    return false;
}

int main()
{
    ifstream input("input.in",ifstream::in);
    ofstream output("output.out",ofstream::out);

    int t;
    input >> t;
    FORI(i,t)
    {
        unsigned long long int A, B;
        input >> A;
        input >> B;


        vector<unsigned long long int> palindromes;
        vector<unsigned long long int> calcpalindromes;
        for(int j = A; j <= B; j++)
        {
            if(palindrome(j)) palindromes.push_back(j);
        }

        for(int j = 0; j < A; j++)
        {
            if(palindrome(j)) calcpalindromes.push_back(j);
        }
        FORI(j,palindromes.size())
        {
            calcpalindromes.push_back(palindromes.at(j));
        }
        FORI(k,calcpalindromes.size())
        {
            unsigned long long int square = calcpalindromes.at(k)*calcpalindromes.at(k);
            if(square > B){calcpalindromes.erase(calcpalindromes.begin()+k,calcpalindromes.end()); break;}
            else{calcpalindromes.at(k) = square;}
        }

        unsigned long long int ct = 0;
        for(int j = 0; j < palindromes.size();j++)
        {
            FORI(k,calcpalindromes.size())
            {
                if(palindromes.at(j) == calcpalindromes.at(k))
                {
                    ct++;
                    break;
                }
            }
        }
        output << "Case #" << i+1 << ": " << ct << endl;
    }
    return 0;
}
