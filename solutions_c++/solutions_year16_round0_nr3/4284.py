#include<iostream>
#include<vector>
#include<math.h>
#include<sstream>
#include<stdint.h>
using namespace std;

vector<int64_t> check_numbers;
vector<int64_t> factors;
bool IsPrime(int64_t num)
{
  for(int64_t i=2;i<1000;i++)
    {
      
      if(num%i==0)
	{
	  factors.push_back(i);
	  return false;
	}
    }
  return true;
}

void find_non_primes(int length)
{
  int max_number=pow(2,length+1)-1;
  int min_number=pow(2,length)+1;
  for(int i=min_number;i<=max_number;i=i+2)
    {
      if(!IsPrime(i))
	{
	  check_numbers.push_back(i);
	}
    }

}
void switch_to_binary()
{
  int length=check_numbers.size();
  for(int i=0;i<length;i++)
    {
      unsigned long ten_base=(unsigned long)check_numbers[0];
      check_numbers.erase(check_numbers.begin());
      int64_t result=0;
      int rem;
       while(ten_base>1)
	{
	  rem=ten_base % 2;
	  ten_base/=2;
	  result+=rem;
	  result*=10;
	}
       result+=ten_base;
       check_numbers.push_back(result);
    }
}

bool check_jam(int64_t num)
{
  stringstream ss;
  string myint64_t;
  
  ss<<num;
  myint64_t=ss.str();
  for(int base=2;base<=10;base++){
    int64_t result=0;
    for(int i=0;i<myint64_t.length();i++)
      {	
	if(myint64_t[i]=='1')
	  {
	    result+=pow(base,myint64_t.length()-1-i);
	  }
      }
	
    if(IsPrime(result))
      {
	return false;
      }
    
  }
  return true;
}


int main()
{

  int case_numbers;
  int length;
  int jam_numbers;
  cin>>case_numbers;
  for(int case_index=0;case_index<1;case_index++){
  cout<<"Case #1:"<<endl;
  cin>>length;
  cin>>jam_numbers;
  find_non_primes(length-1); 
  int jam_index=0;
  
  switch_to_binary();
    
  
  for(int i=0;i<check_numbers.size()&&jam_index<jam_numbers;i++)
    {
      factors.clear();
      
      if(check_jam(check_numbers[i]))
      {
	stringstream ss;
	string mynumber;
	ss<<check_numbers[i];
	mynumber=ss.str();
	cout<<mynumber<<" ";
	jam_index++;
	for(int j=0;j<factors.size();j++)
	{
		cout<<factors[j]<<" ";
		
	}
	
	cout<<endl;
	
      }
    }
  }
  return 0;
}
