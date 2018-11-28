#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>

using namespace std;

#define CASE "Case #"

double A,B;
int count=0;

bool is_square(int num)
{
  double d_result=sqrt(num);
  int i_result = (int)d_result;
  
  if((i_result*i_result) == num) return true;
  else return false;
}


bool is_palindrome(int num)
{
  int temp, r, sum;
  
    temp=num;
    sum=0;
    
    while(temp)
    {
      r=temp%10;
      temp=temp/10;
      sum=sum*10+r;
    }
    if(num == sum) true;
    else return false;  
}

int main(int argc, char* argv[])
{
  ifstream in_file(argv[1]);
  ofstream out_file("Output");
  
  if(!in_file.is_open())
  {
    cout<<"Unable to open Output file"<<endl;
    exit(1);
  }
  
  int T;
  bool status1, status2;
  
  in_file>>T;
  
  for(int i=0; i<T; i++)
  {
    in_file>>A>>B;
    
    count = 0;
    
    for(int number=A; number<=B; number++)
    {
      if(is_square(number))
      {
	status1 = is_palindrome(number);
	status2 = is_palindrome(sqrt(number));
	if(status1 == true && status2 == true) count++;
      }
    }
    
    out_file<<CASE<<i+1<<": "<<count<<endl;
  }
  
  return 0;
}