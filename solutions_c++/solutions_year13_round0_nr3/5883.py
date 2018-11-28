#include <iostream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <utility>
#include <vector>
#include <pthread.h>
#include <cstring>

#define DEB(x) std::cerr<<"TaChIdOk: "<<#x<<":("<<x<<")"<<std::endl
#include <typeinfo>
#define T_TYPE(x) DEB(typeid(x).name())
#define T_ERROR() std::cerr<<"TaChIdOk's error on"<<std::endl<<std::endl<<"\tFile: "<<std::endl<<std::endl<<"\t"<<__FILE__<<std::endl<<std::endl<<"\tLine: "<<std::endl<<std::endl<<"\t"<<__LINE__<<std::endl<<std::endl<<"\tFunction: "<<std::endl<<std::endl<<"\t"<<__PRETTY_FUNCTION__<<std::endl<<std::endl; terminate()
#define T_ERROR2(x) throw ("Error at function "+string(__PRETTY_FUNCTION__)+": "+string(x))
#define T_WARNING(x) cerr << (string("Warning at function ") + string(__PRETTY_FUNCTION__) + ": " + string(x))
#define T_SUCCESS(x) cerr<<(string(__PRETTY_FUNCTION__)+string(x))<<endl

bool is_palindrome(unsigned C);

int main(int argc, char *argv[])
{
 char filename[100];
 sprintf(filename, "output.txt");
 FILE *file_pt = fopen(filename, "w");

 unsigned ncases = 0;
 scanf("%d\n", &ncases);
 DEB(ncases);

 for (unsigned icase = 0; icase < ncases; icase++)
  {
   unsigned nfair_square = 0;
   unsigned A, B, C;
   scanf("%d %d\n",&A,&B);

   // DEB("#######################");
   // DEB(icase);
   // DEB("#######################");
   for (unsigned i = 1; i <= B; i++)
    {
     C = i*i;
     if (C >= A && C <= B)
      {
       // DEB(i);
       bool ipalindrome = is_palindrome(i);
       if (ipalindrome)
        {
         // DEB(C);
         bool Cpalindrome = is_palindrome(C);
         if (Cpalindrome)
          {
           nfair_square++;
          }
        }
      }
    };
   fprintf(file_pt, "Case #%d: %d\n",icase+1,nfair_square);
  }
 fclose(file_pt);
}

bool is_palindrome(unsigned D)
{
 char pal[20];
 sprintf(pal,"%u",D);
 std::string str(pal);
 unsigned nstr = str.size();
 // DEB(D);
 // DEB(nstr);
 int leftc = 0;
 int rightc = nstr-1;
 while(leftc<=rightc)
  {
   // DEB(str[leftc]);
   // DEB(str[rightc]);
   if (str[leftc]!=str[rightc])
    {
     // DEB("false");
     return false;
    }
   leftc++;
   rightc--;
  }
 // DEB("true");
 return true;
}

