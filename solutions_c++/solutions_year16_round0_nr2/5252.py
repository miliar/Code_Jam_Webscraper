#include<iostream>
#include<algorithm>
using namespace std;
int find_minus(string str)
{
  for(int i=str.length()-1;i>=0;i--)
    {
      if(str[i]=='-')
	{
	  return i;
	}
    }
  return -1;
}
//if the first place is plus, then find the series of plus and flip it.
int get_pluses(string str)
{
  for(int i=0;i<str.length();i++)
    {
      if(str[i]=='-')
	{
	  return i-1; 
	}
    }
  return -1;
}
string flip(string str, int end)
{
  string new_string;
  string substr=str.substr(0,end+1);
  string substr2=str.substr(end+1);
  std::reverse(substr.begin(),substr.end());
  for(int i=0;i<substr.length();i++)
    {
      if(substr[i]=='+')
	{
	  substr.replace(i,1,1,'-');
	}
      else{
	
	substr.replace(i,1,1,'+');
      }
  }
  new_string=substr+substr2;
  return new_string;
}


int flip_turns(string str)
{
  int turn =0;
  int minus_index=find_minus(str);
  while(minus_index>=0&&turn<=100)
    {
      if(str[0]=='+')
	{
	  int end=get_pluses(str);
	  str=flip(str,end);
	  turn++;
	}
      str=flip(str,minus_index);
      turn++;
      minus_index=find_minus(str);
    }
  return turn;
}
int main()
{
  int case_numbers;
  cin>>case_numbers;
  int case_index=1;
  for(int i=1;i<=case_numbers;i++){
    string pancakes;
    cin>>pancakes;
    int result=flip_turns(pancakes);  
    cout<<"Case #"<<i<<": "<<result<<endl;
  }
}
