#include <iostream>
using std::cout;
using std::cin;
using std::endl;

#include <string>
using std::string;
using std::getline;

#include <vector>
using std::vector;

#include <cmath>

#include <boost/lexical_cast.hpp>

inline bool ispal( long long n, long long *add = NULL )
{
  string num = boost::lexical_cast< string >(n);
  long long len = num.size();
  for( long long i = 0; i < (len / 2); ++i )
  {
    if( num[i] != num[len-i-1] )
    {
      if( add != NULL )
      {
        *add = 1;
        while( i )
        {
          *add = *add * 10;
          --i;
        }
      }
      return false;
    }
  }
  return true;
}

void handle( int n )
{
  long long a,b,add = 0;
  cin >> a >> b;
  long long maxroot = sqrt(b);
  long long minroot = ceil(sqrt(a));
  long long i = minroot;
  long long num = 0;

  while( i <= maxroot )
  {
    add = 1;
    if( ispal( i, &add ) && ispal( i*i ) )
    {
      num++;
      ++i;
    }
    else
    {
      i = i + add;
    }
  }

  cout << "Case #" << n << ": " << num << endl;
}

int main(int argc, char *argv[])
{
  int N;
  string line;
  cin >> N;
  getline( cin, line );
  for( int i = 1; i <= N; ++i ) handle( i );
  
  return 0;
}

