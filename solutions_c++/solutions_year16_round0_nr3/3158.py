
#include <iostream>     // std::cout
#include <fstream>      // std::ifstream
#include <sstream>      // std::ifstream
#include <string>
#include <vector>
//#include <list>
//#include <ctime>
#include <QtDebug>
#include <limits>
#include <cmath>


void generateJamcoins(unsigned amount, std::vector<std::string>& resultJamCointVector, std::vector<std::vector<unsigned long long> >& resultDivisorsVector);
unsigned long long getDecimalNumberFromJamcoin(int base);
void nextJamcoin();
bool isPrime(unsigned long long n, unsigned long long& divisor);

static std::string baseJamCoin;

int main(int argc, char *argv[])
{

   unsigned int T = 0;
   unsigned int N = 0;
   unsigned int J = 0;

   std::ifstream ifs ("Input.txt", std::ifstream::in);



   std::string line;
   std::vector<std::string> numbers;

   if(std::getline(ifs, line))
   {
       std::istringstream iss(line);
       iss >> T;
   }

   if(std::getline(ifs, line))
   {
       std::istringstream iss(line);
       iss >> N >> J;
   }

   ifs.close();

   baseJamCoin.insert(0, N-2, '0');
   baseJamCoin.insert(0, 1, '1');
   baseJamCoin.insert(baseJamCoin.size(), 1, '1');
   std::cout << T << N << J << " " << baseJamCoin <<" \n";


   std::vector<std::string> resultJamCointVector;
   resultJamCointVector.reserve(J);

   std::vector<std::vector<unsigned long long> > resultDivisorsVector;
   resultDivisorsVector.reserve(J);

   generateJamcoins(J, resultJamCointVector, resultDivisorsVector);



   std::ofstream ofs ("Output.txt", std::ofstream::out);

   std::cout << "resultVector : \n";

   ofs << "Case #1:" << "\n";

   for(int i = 0; i<resultJamCointVector.size(); i++)
   {
       ofs << resultJamCointVector[i];

       for(int j = 0; j<resultDivisorsVector[i].size(); j++)
       {
           ofs << " " << resultDivisorsVector[i][j];
       }

       ofs << "\n";
   }

   ofs.close();

   return 0;
}


void generateJamcoins(unsigned amount, std::vector<std::string>& resultJamCointVector, std::vector<std::vector<unsigned long long> >& resultDivisorsVector)
{
    while(resultJamCointVector.size() < amount)
    {
         std::cout << "!!!!generateJamcoins: "<< resultJamCointVector.size() << " " << amount <<" \n";
        nextJamcoin();

        std::vector<unsigned long long> divisors;

        for(int i = 2; i<=10; i++)
        {
            unsigned long long divisor;
            if(isPrime(getDecimalNumberFromJamcoin(i), divisor))
                break;
            else
            {
                divisors.push_back(divisor);
            }
        }

        if( divisors.size() == 9 )
        {
            resultJamCointVector.push_back(baseJamCoin);
            resultDivisorsVector.push_back(divisors);
        }
    }
}

unsigned long long getDecimalNumberFromJamcoin(int base)
{
    unsigned long long decimalNumber = 0;
    int jamCoinLength = baseJamCoin.length();

    for(int i = jamCoinLength-1; i >= 0; i--)
    {
        if(baseJamCoin[i] == '1')
        {
            decimalNumber += pow(base, jamCoinLength - i - 1);
        }
    }

    return decimalNumber;
}


void nextJamcoin()
{
    for(int i = baseJamCoin.length()-1; i >= 0; i--)
    {
        if(baseJamCoin[i] == '0')
        {
           baseJamCoin[i] = '1';

            for(int j = baseJamCoin.length()-2; j > i; j--)
            {
                baseJamCoin[j] = '0';
            }

            break;
        }
    }

}

bool isPrime(unsigned long long n, unsigned long long& divisor){
    for(unsigned long long i=2;i<=sqrt(n);i++)
        if(n%i==0)
        {
            divisor = i;
            return false;
        }
    return true;
}

