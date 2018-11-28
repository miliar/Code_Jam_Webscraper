#include <iostream>
#include <fstream>
#include <string>
#include <bitset>
#include <vector>

class Jamcoin
{
    public:
        std::string name;
        std::vector<int> divisors [9]; // 2-10.
        void print()
        {
            std::cout << "name: " << name << "\n";
            std::cout << "divisors: \n";
            for(int i = 2; i <=10; i ++)
            {
                std::vector<int> divisor = divisors[i-2];
                for(std::vector<int>::iterator iter = divisor.begin(); iter != divisor.end(); iter++)
                {
                    std::cout << *iter << " ";
                }
                std::cout << std::endl;
            }
        }
};

void all4bits(int base_values[][8], int* primes);

std::vector<int> divisor(std::string digits, int base, int base_values[][8], int* primes);

int main()
{
    // In & out.
    std::ifstream in;
    std::ofstream out;

    // Open files.
    in.open("C-small-attempt0.in");
    out.open("C-small-attempt0.out");

    // Global variables.
    int T, N, J;

    // base_values are frequently used.(2-10, 0-8)
    int base_values[9][8];
    for(int i = 0; i < 9; i ++)
    {
        base_values[i][0] = 1;
        for(int j = 1; j < 8; j ++)
        {
            base_values[i][j] = base_values[i][j-1] * (i+2);
        }
    }

    // Primes
    int primes[31] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127};

    in >> T >> N >> J;
    out << "Case #1:" << std::endl;

    // The following have common factor series.
    std::string fix6[5] = {"100001", "100111", "101101", "110011", "111001"};
    std::string fix4[2] = {"1111", "1001"};

    // Print for small dataset.
    while(J > 0)
    {
        for(int i = 0; i < 5; i ++)
        {
            for(int j = 0; j < 5; j ++)
            {
                for(int k = 0; k < 2; k ++)
                {
                    out << fix6[i] << fix6[j] << fix4[k];
                    out << " 3 2 5 2 7 2 3 2 11" << std::endl;
                    J--;
                }
            }
        }
    } 

    //all4bits(base_values, primes);
    // Close files.
    out.close();
    in.close();

    return 0;
}

// Given digits starts and ends with '1',
// and base between 2 and 10.
// Return all divisors.
std::vector<int> divisor(std::string digits, int base, int base_values[][8], int* primes)
{
    std::vector<int> divisors;

    int sum = 0;
    // Only process 6-width digits.
    for(int i = 0; i < 6; i ++)
    {
        sum += (digits[i]-48) * base_values[base-2][5-i];
    }

    //std::cout << "sum under "<< base << " is " << sum << ",";

    // Find all divisors.
    int i = 0;
    while(i < 31) // Exceedes then is considered as prime number.
    {
        if(sum != primes[i] && sum % primes[i] == 0)
        {
            divisors.push_back(primes[i]);
            sum /= primes[i];
        }else
        {
            i ++;
        }
    }

    return divisors;

}

void all4bits(int base_values[][8], int* primes)
{
    std::vector<Jamcoin> jamcoins;

    //
    for(int i = 1; i < 64; i ++) // A special case "0000".
    {
        Jamcoin jamcoin;
        bool effect_jam = true;

        std::string unit = std::bitset<6>(i).to_string();
        jamcoin.name = unit;

        for(int j = 2; j <= 10; j ++)
        {
            std::vector<int> divisors = divisor(unit, j, base_values, primes);
            if(divisors.empty())
            {
                effect_jam = false;
                break;
            }
            jamcoin.divisors[j - 2] = divisors;
        }
        if(effect_jam)
        {
            jamcoins.push_back(jamcoin);
            jamcoin.print();
        }
    }

}
