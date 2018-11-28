#include <fstream>
#include <iostream>
#include <cstdlib>
#include <cmath>
using namespace std;

long long factorial( long long n, long long k = 1 )
{
  if( n <= k )
  {
    return 1;
  }
  else
  {
    return n * factorial(n-1, k);
  }
}

long long choose( long long n, long long k )
{
  if( k >= n-k )
  {
    return factorial(n, k) / factorial(n-k);
  }
  else
  {
    return factorial(n, n-k) / factorial(k);
  }
}

int main( int argc, char** argv )
{
  if( argc != 3 )
  {
    cout << "Mark, idiot, use parameters!" << endl;
    exit(1);
  }
  ifstream fin(argv[1]);
  ofstream fout(argv[2]);
  unsigned int T;
  fin >> T;

  for( unsigned int i = 0; i < T; i++ )
  {
    if( i != 0 )
    {
      fout << "\n";
    }
    fout << "Case #" << i+1 << ": ";
    long long X, Y, N;
    fin >> N >> X >> Y;
    if( X < 0 )
    {
      X = -X;
    }
    long long height = (X + Y) / 2;
    long long preReq = (2 * height - 1) * height;
    long long nextFullLevel = 2*height*height + 3*height + 1;
    long long stackGoal = Y + 1;
    if( X == 0 )
    {
      stackGoal = Y * 2 + 1;
    }
    if( N < preReq + stackGoal )
    {
      fout << "0.0";
    }
    else if( N >= preReq + height*2 + Y + 1 )
    {
      fout << "1.0";
    }
    else
    {
      long long remainingToStack = N - preReq;
      double answer = pow(.5, remainingToStack);
      long long accumulator = 0;
      for( long long j = stackGoal; j <= remainingToStack; j++ )
      {
        accumulator += choose(remainingToStack, j);
      }
      answer *= accumulator;
      fout << answer;
    }
  }

  fin.close();
  fout.close();
  return 0;
}