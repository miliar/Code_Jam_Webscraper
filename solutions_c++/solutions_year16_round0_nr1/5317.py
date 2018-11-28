#include <iostream>
#include <sstream>
#include <string>
using namespace std;

string intTostring(int i)
{
  ostringstream conv;
  conv << i;
  return conv.str();
}

int charToInt(char c)
{
  if(c == '0')
	return 0;
  if(c == '1')
	return 1;
  if(c == '2')
	return 2;
  if(c == '3')
	return 3;
  if(c == '4')
	return 4;
  if(c == '5')
	return 5;
  if(c == '6')
	return 6;
  if(c == '7')
	return 7;
  if(c == '8')
	return 8;
  if(c == '9')
	return 9;
  
}

int main()
{
  
  int cases;
  int N;
  bool check[10];
  int j; //iterator
  int counter;
  string str;
  bool done;
  cin >> cases;
  for(int i = 1; i <= cases; i++)
  {
    cin >> N;
	cout << "Case #" << i << ": ";
	//check for insomnia
	
	if(N == 0)
	  cout << "INSOMNIA" << endl;
	//
	//else find last number
	else
	{
	  for(j = 0; j < 10; j++)
	    check[j] = false;
	  done = false;
	  counter = 1;
	  str = intTostring(N);
	  for(j = 0; j < str.size(); j++)
	    check[charToInt(str[j])] = true;
	  while(!done)
	  {
	    counter++;
		str = intTostring(N * counter);
		for(j = 0; j < str.size(); j++)
        {			
	      check[charToInt(str[j])] = true;
		}
		done = true;
	    for(j = 0; j < 10; j++)
		{
		  if(check[j] == false)
		  {
			done = false;
			break;
		  }
	    }
	  }
	  cout << str << endl;
	}
  }
  return 0;
}