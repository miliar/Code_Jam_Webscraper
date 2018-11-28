
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
#include <ios>
#include <iomanip>

long double calculateFirstLastGoldTiles(int k, int c);
std::vector<std::vector<long double> > calculateGoldTiles(const std::vector<std::tuple<int, int, int> >& numbers);

unsigned int T = 0;

int main(int argc, char *argv[])
{

   std::ifstream ifs ("Input.txt", std::ifstream::in);


   std::string line;

   if(std::getline(ifs, line))
   {
       std::istringstream iss(line);
       iss >> T;
   }

   std::vector<std::tuple<int, int, int> > numbers;
   numbers.reserve(T);


   while(std::getline(ifs, line))
   {
      std::istringstream iss(line);

      unsigned int K = 0;
      unsigned int C = 0;
      unsigned int S = 0;

      iss >> K >> C >> S;

      auto t = std::make_tuple(K, C, S);
      numbers.push_back(t);
   }

   ifs.close();



   std::vector<std::vector<long double> > resultVector;
   resultVector = calculateGoldTiles(numbers);


   std::ofstream ofs ("Output.txt", std::ofstream::out);

   ofs.setf(std::ios_base::fixed);

   std::cout << "resultVector : \n";
   for (int i =1; i<=T; i++)
   {
       std::cout << "resultVector :" << i << "\n";
       std::cout << "resultVector : 1" << resultVector[i-1].size() << "\n";
       std::cout << "resultVector : 2" << std::get<2>(numbers[i-1]) << "\n";
      //std::cout << resultVector[i-1]  <<" \n";
      ofs << "Case #" << i << ":";

      ofs << std::setprecision(0);

      if( (resultVector[i-1].size() <= std::get<2>(numbers[i-1])) && //tries < s
           resultVector[i-1].size() != 0 )
      {
          for (int j =0; j<resultVector[i-1].size(); j++)
          {
              ofs << " " << resultVector[i-1][j];
          }
      }
      else
          ofs << " IMPOSSIBLE";

      if(i!=T)
          ofs << "\n";
   }

   ofs.close();

   return 0;
}

std::vector<std::vector<long double> > calculateGoldTiles(const std::vector<std::tuple<int, int, int> >& numbers)
{
    std::vector<std::vector<long double> > resultVector;

    std::cout << "calculateGoldTiles :" << "\n";

    for(int i = 0; i<T; i++)
    {
        std::cout << "calculateGoldTiles :" << i <<"\n";
        unsigned k = std::get<0>(numbers[i]);
        unsigned c = std::get<1>(numbers[i]);
        unsigned s = std::get<2>(numbers[i]);

        std::vector<long double> currentArtwork;

        if(c == 1)
        {
            if(s>=k)
            {
                for(int y = 1; y <= k; y++)
                {
                    currentArtwork.push_back(y);
                }
            }
        }
        else
        {


        long double firslastTilesNumber = calculateFirstLastGoldTiles(k,c);

        std::cout << "calculateGoldTiles 1:" << i << " " << firslastTilesNumber <<"\n";
        long double wholeLine = pow(k,c);

        std::cout << "calculateGoldTiles 2:" << i << " " <<wholeLine <<"\n";

        if(firslastTilesNumber < wholeLine)
        {
            if(firslastTilesNumber*2 > wholeLine)
            {
                currentArtwork.push_back(firslastTilesNumber);
                //1 try, middle element (firslastTilesNumber)
            }
            else
            {
                currentArtwork.push_back(firslastTilesNumber);
                currentArtwork.push_back(wholeLine - firslastTilesNumber + 1);

//                for(long double z = 0; z < pow(k, c-1); z = z+k)
//                {
//                    std::cout << "calculateGoldTiles 3:" << z << " " << pow(k, c-1) <<"\n";
//                    if( ( firslastTilesNumber < k*(z-1) ) &&
//                        ( (wholeLine - firslastTilesNumber + 1) > k*z ) )
//                    {
//                        currentArtwork.push_back(k*z);
//                    }
//                }

                std::cout << "calculateGoldTiles x:" <<"\n";
                //long double firstMiddleNumber = 1.0;
                long double firstMiddleNumber = trunc(firslastTilesNumber/pow(k, c-1))+2;
                //long double firstMiddleNumber = (firslastTilesNumber - 1.0)/k + 2;

//                for(long double z = firslastTilesNumber/k; z < pow(k, c-1); z = z+1.0)
//                {
//                    if( firslastTilesNumber < k*(z-1) )
//                        firstMiddleNumber = z;
//                        //currentArtwork.push_back(k*z);
//                }




                //long double lastMiddleNumber = 1.0;
                //long double lastMiddleNumber = (wholeLine - firslastTilesNumber + 1)/k - 1;
                long double lastMiddleNumber = trunc((wholeLine - firslastTilesNumber)/pow(k, c-1));//  trunc(wholeLine - firslastTilesNumber)/k - 1;
                std::cout << "calculateGoldTiles xx: " << wholeLine << " " << firslastTilesNumber << " "<<k << " " << lastMiddleNumber << "\n";

//                for(long double z = pow(k, c-1); z > 0; z = z-1.0)
//                {
//                    if( (wholeLine - firslastTilesNumber + 1) > k*z )
//                        lastMiddleNumber = z;
//                        //currentArtwork.push_back(k*z);
//                }

                if((lastMiddleNumber - firstMiddleNumber) > s)
                {
                    currentArtwork.clear();
                }
                else
                {

                    std::cout << "calculateGoldTiles xxx:" << firstMiddleNumber << " " << lastMiddleNumber << "\n";
                    for(long double z = firstMiddleNumber; z <= lastMiddleNumber; z = z+1.0)
                    {
                        currentArtwork.push_back(pow(k, c-1)*z);
                    }

                    //            firslastTilesNumber + (wholeLine - firslastTilesNumber) +
                    //                    middle elements (k*1 +1), (k*2 +1),  ... (k*(c - 1) +1)
                    //                    - numbers that set in firstlast

                }
            }
        }
        else
            currentArtwork.push_back(1);
        //1 try, first tile;

        }


        resultVector.push_back(currentArtwork);
    }

    return resultVector;
}

long double calculateFirstLastGoldTiles(int k, int c)
{
    long double amountOfFirstGoldTiles = 1.0;

    if( c > 1 )
        amountOfFirstGoldTiles = k + 1.0;


    for(int i = 2; i<c; i++)
    {
        amountOfFirstGoldTiles = amountOfFirstGoldTiles*k + 1;
    }

    return amountOfFirstGoldTiles;
}
