#include<stdio.h>
#include<iostream>
#include<string.h>
#include<math.h>


using namespace std;
bool palindrome(unsigned long long int passed){
unsigned long long int reversed = 0,passed_copy;

 passed_copy=passed;
   while (passed != 0)
   {
      reversed = reversed * 10;
      reversed = reversed + passed%10;
      passed = passed/10;
   }
   if (passed_copy==reversed)
   return true;
   else
   return false;
}



int main()
{

int testcases;
unsigned long long int a,b,i;
int count=0;


cin>> testcases;
for(int j=0;j<testcases;j++){
    cin >> a >> b;
for(unsigned long long int i=a;i<=b;i++){
if(palindrome(i)){
if(sqrt(i)==int(sqrt(i)))
if(palindrome(sqrt(i)))
count++;
}
}
int l=j+1;
cout << "Case #"<< l<< ": "<< count << endl;
count=0;
}





return 0;
}
