
#include <iostream>     // std::cout
#include <fstream>      // std::ifstream
#include <sstream>      // std::ifstream
#include <string>
#include <vector>
//#include <list>
//#include <ctime>
#include <QtDebug>
#include <limits>

unsigned long long countNumbers(unsigned long N);
void getDigitsFromNumber(unsigned long N, std::vector<unsigned char>& digitsVector);
bool allDigitsPresent(const std::vector<unsigned char>& digitsVector);

int main(int argc, char *argv[])
{

   unsigned int T = 0;
   unsigned long N = 0;

   std::ifstream ifs ("Input.txt", std::ifstream::in);



   std::string line;
   std::vector<unsigned long> numbers;

   if(std::getline(ifs, line))
   {
       std::istringstream iss(line);
       iss >> T;
   }

   while(std::getline(ifs, line))
   {
      std::istringstream iss(line);

      iss >> N;
      numbers.push_back(N);
   }

   ifs.close();


   std::vector<unsigned long long> resultVector;
   resultVector.reserve(T);

   for (int i =1; i<=T; i++)
   {
      resultVector.push_back(countNumbers(numbers[i-1]));
   }


   std::ofstream ofs ("Output.txt", std::ofstream::out);

   std::cout << "resultVector : \n";
   for (int i =1; i<=T; i++)
   {
      std::cout << resultVector[i-1]  <<" \n";
      ofs << "Case #" << i << ": ";
      if( 0 == resultVector[i-1])
          ofs << "INSOMNIA" ;
      else
          ofs << resultVector[i-1] ;

      if(i!=T)
          ofs << "\n";
   }

   ofs.close();

   return 0;
}


unsigned long long countNumbers(unsigned long N)
{
    std::vector<unsigned char> digits = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

    int i = 0;

    unsigned long long currentN;

    while( i <= 100 &&
           !allDigitsPresent(digits) )
    {
        i++;
        if(N * i <= std::numeric_limits<unsigned long long>::max())
        {
            currentN = N * i;
        }
        else
        {
            return 0;
        }
        //qDebug() << "current N " <<currentN;

        getDigitsFromNumber(currentN, digits);
    }

    return currentN;
}

void getDigitsFromNumber(unsigned long N, std::vector<unsigned char>& digitsVector)
{
    while( N != 0 )
    {
        unsigned char n = N % 10;
        digitsVector[n] = 1;

        N/=10;
    }
}

bool allDigitsPresent(const std::vector<unsigned char>& digitsVector)
{
    for(auto i: digitsVector)
    {
        if( 0 == i )
            return false;
    }

    return true;
}

