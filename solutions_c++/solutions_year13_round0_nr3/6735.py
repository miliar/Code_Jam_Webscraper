#include<iostream>
#include<math.h>
#include<fstream>
#include <cmath>

using namespace std;

int lengthfunction(int number)
{    
      int counter=0;
      while(number)
     {        
            number=number/10;
            counter++;
      }
      return (counter);
}

bool forSquare(long num){
      
      long temp = num; //Value of temp stores unmodified n value
       long remainder;
       long sum=0;
  while(num>0)
    {
      remainder=num%10; 
      num/=10;                
     sum=sum*10 + remainder; //Builds value of reversed number
     }

   if (sum==temp)
     return true;
   else
     return false;
   
}
     
     
int main(){

      fstream f;
      ofstream output("ouput.txt");
      f.open("C-small-attempt0.in");
      long Cases;
      long counter=0;
      long count=1;
      f>>Cases;
      long a , b;
      while(Cases>0){
        f>>a;
        f>>b;
        for(long i = a ; i<=b ;i++){
                 if(std::floor(sqrt(i)) == sqrt(i)){
                if(forSquare(i)&&forSquare(sqrt(i)) == true)
                {

                   cout<<i<<"  " <<sqrt(i)<<endl;
                   counter++;                                                
                                                }
                 }
                 }
          output<<"Case #"<<count<<": "<<counter<<endl;
               count++;
               counter=0;
          Cases--;        
                  }
                              
                
system("pause");
}        

