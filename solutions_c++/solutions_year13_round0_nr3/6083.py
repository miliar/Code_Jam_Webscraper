#include <iostream>
#include <fstream>
#include <cmath>
#include <string>

using namespace std;

int power10(int d)
{
  int answer = 1;
  for(int i=0; i < d; ++i)
    answer*=10;
  return answer;
}

bool isPalin(int current)
{
  string test = "";
  if(current < 10)
    return true;
  while(current > 0)
  {
    test.push_back(current%10+'0');
	current/=10;
  }
  for(int i=0; i <= test.size()/2; ++i)
    if(test[i] != test[test.size()-i-1])
	  return false;
  return true;
}

int main()
{
  ifstream myfile ("C-small-attempt0.in");
  ofstream answer ("1C.out");
  int cases, start, end, count;
  
  myfile >> cases;
  
  for(int c=0; c < cases; ++c)
  {
    myfile >> start >> end;
	count = 0;
	for(int i=sqrt(1.0*start); i <= sqrt(1.0*end); ++i)
	  if(isPalin(i) && isPalin(i*i) && i*i >= start)
	  {
	    ++count;
	  }
	answer << "Case #" << c+1 << ": " << count << endl;
  }
  
  return 0;  
}
