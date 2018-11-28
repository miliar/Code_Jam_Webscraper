
#include <iostream>     // std::cout
#include <fstream>      // std::ifstream
#include <sstream>      // std::ifstream
#include <string>
#include <vector>
//#include <list>
//#include <ctime>
#include <QtDebug>
#include <limits>

unsigned long countFlips(std::string& flips);
bool allSymbolsTheSame(const std::string& flips, char& symbol);

int main(int argc, char *argv[])
{

   unsigned int T = 0;
   std::string S;

   std::ifstream ifs ("Input.txt", std::ifstream::in);



   std::string line;
   std::vector<std::string> numbers;

   if(std::getline(ifs, line))
   {
       std::istringstream iss(line);
       iss >> T;
   }

   while(std::getline(ifs, line))
   {
      std::istringstream iss(line);

      iss >> S;
      numbers.push_back(S);
   }

   ifs.close();


   std::vector<unsigned long long> resultVector;
   resultVector.reserve(T);

   for (int i =1; i<=T; i++)
   {
      resultVector.push_back(countFlips(numbers[i-1]));
   }


   std::ofstream ofs ("Output.txt", std::ofstream::out);

   std::cout << "resultVector : \n";
   for (int i =1; i<=T; i++)
   {
      std::cout << resultVector[i-1]  <<" \n";
      ofs << "Case #" << i << ": " << resultVector[i-1] ;

      if(i!=T)
          ofs << "\n";
   }

   ofs.close();

   return 0;
}


unsigned long countFlips(std::string& flips)
{
    unsigned long counter = 0;

    char allSymbol;
    while(!allSymbolsTheSame(flips, allSymbol))
    {
        char firstChar = flips.front();
        for(long i = 1; i<flips.length(); i++)
        {
            if(flips[i] != firstChar)
            {
                for(long j = 0; j<i; j++)
                {
                    flips[j] = flips[i];
                }
                counter++;
                break;
            }
        }
    }

    if(allSymbol == '-')
        counter++;

    return counter;
}

bool allSymbolsTheSame(const std::string& flips, char& symbol)
{
    symbol = flips.front();
    for(auto i: flips)
    {
        if( symbol != i )
            return false;
    }

    return true;
}

