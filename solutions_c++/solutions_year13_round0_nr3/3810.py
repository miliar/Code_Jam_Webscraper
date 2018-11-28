#include <iostream>
#include <string>
#include <utility>
#include <cmath>

#include <stdio.h>
#include <string.h>
#include <sstream>

class FairSquare
{
      typedef unsigned long long uint_64;
      std::pair<uint_64, uint_64> range;
      std::pair<uint_64, uint_64> root_range;
      
      uint_64 nextPalindrome(const uint_64 num)
      {
              //std::cout << "nextPalindrome("<<num<<")"<<std::endl;
          if (num < 8) return num+1;
          uint_64 number;
          char word[51];
          sprintf(word, "%llu", num);
          const size_t len = strlen(word);
          bool all_9 = true;
          for(int iii = 0; iii < len ; ++iii) ///all 9999s
          {
              if( word[iii] == '9' ) continue;
              all_9 = false;
              break;
          }
          if(all_9) return num+2;
          
          const size_t half_len = len/2;
          char half_word[51];
          strcpy(half_word, word);
          half_word[half_len+len%2]='\0';
          uint_64 half_number;
          std::istringstream ( half_word ) >> half_number;
          do{
              sprintf(half_word, "%llu", half_number);
              for(int iii = 0; iii < half_len ; ++iii)
              {
                  half_word[len-1-iii] = half_word[iii];// creating full word
              }
              half_word[len]='\0';
              std::istringstream ( half_word ) >> number;
              ++half_number;
          } while ( number <= num );
          return number;
      }
      
      bool isPalindrome(const uint_64 num)
      {
          if (num < 10) return true;
          uint_64 number;
          char word[51];
          sprintf(word, "%llu", num);
          const size_t len = strlen(word);
          const size_t half_len = len/2;
          for(int iii = 0; iii < half_len ; ++iii)
          {
              if( word[iii] == word[len-1-iii]) continue;
              return false;
          }
          return true;
      }
public:
       void readRange()
       {
            std::cin >> range.first;
            std::cin >> range.second;
            root_range.first = sqrt(range.first);
            if ( ( root_range.first * root_range.first ) < range.first ) ++ root_range.first;
            root_range.second = sqrt(range.second);
       }
       
       void getCount(int testid)
       {
            uint_64 count=0;
            uint_64 num = nextPalindrome(root_range.first-1);
            
            for( ; num <= root_range.second; num = nextPalindrome(num))
            {
                uint_64 sq_num = num * num;
                if(sq_num >= range.first && sq_num <= range.second && isPalindrome(sq_num))
                {
                    //std::cout << num << " " << sq_num << std::endl;
                    ++count;
                }
                //else
                    //std::cout << num << " -" << std::endl;
            }
            
            //std::cout <<range.first<< " " << range.second << " Case #" << testid << ": " << count << std::endl;
            std::cout << "Case #" << testid << ": " << count << std::endl; 
       }
};

int main()
{
    int testcases;
    std::cin >> testcases;
    
    for(int iii = 1; iii <= testcases; ++iii)
    {
        FairSquare solver;
        solver.readRange();
        solver.getCount(iii);
    }
        
    return 0;
}
