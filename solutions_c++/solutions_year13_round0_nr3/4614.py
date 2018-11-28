#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

bool isPerfectSquare(int num)
{
  double sqroot = (sqrt(num) );
  return sqroot*sqroot == num;
}

bool is_palindrome(int num){
     int digit;
     int original = num;
     int reverse = 0;
      while (num > 0)
      {
      digit = num % 10;
      reverse = reverse * 10 + digit;
      num = num / 10;
       }
     if (original==reverse){return true;}
     return false;
}

int main(){
    int a,b,c,d,e;
    std::ifstream in ("fair and square.in");
    std::ofstream out ("fair and square.out");
    int quantity;
    in >> quantity;
    for (int i=0;i<quantity;i++){        
        int min,max;
        in>>min;
        in>>max;
        int count=0;
        for (int j=min;j<=max;j++){
            if (is_palindrome(j) ){
               if (isPerfectSquare(j)){
                  if (is_palindrome((int)sqrt(j))){
                                 count+=1;
                  }
               }
            }
            
            
        }
        out<<"Case #"<<(i+1)<<": "<<count<<"\n";
    }
    
    
}
