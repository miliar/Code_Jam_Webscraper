#include<iostream>
#include<algorithm>
#include<vector>
#include<sstream>
#include<string>
using namespace std;
#define LIMIT_N 200;
vector<int> digits;

bool find(vector<int> digits,int num)
{
  for(int i=0;i<digits.size();i++)
    {
      if(digits[i]==num)return true;
    }
  return false;
}

long count_sheep(long start_number)
{
  
  long turn=1;
  long end_number=-1;
  long this_number;
  for(turn=1;turn<=100;turn++)	
    {
       this_number=start_number*turn;
      string mylong;
      stringstream mystream;
      mystream<<this_number;
      mylong=mystream.str();
      for(int i=0;i<10;i++){
	stringstream mystreamint;
  	mystreamint<<i;
        string myint=mystreamint.str();
	if(!find(digits,i)){
	  if(mylong.find(myint)!=std::string::npos){
	    digits.push_back(i);
	  }
	}
	if(digits.size()==10){
	  end_number=this_number;
	 
	  return end_number;
	}
      }
     
      
    }
  return end_number;
}


int main()
{
  int case_numbers;
  cin>>case_numbers;
  int case_index=1;
  for(int i=1;i<=case_numbers;i++){
    digits.clear();
    long start_number;
    cin>>start_number;
    long end_number=count_sheep(start_number);  
    if(end_number>0){
      cout<<"Case #"<<i<<": "<<end_number<<endl;
    }else{
      cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
    }
  }
}
