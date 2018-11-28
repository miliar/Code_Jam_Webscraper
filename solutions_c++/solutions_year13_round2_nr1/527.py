#include <fstream>
#include <iostream>
#include <cstdlib>
#include <vector>
using namespace std;

void sort( vector<unsigned long>& v )
{
  for( unsigned long i = 0; i < v.size(); i++ )
  {
    for( unsigned long j = v.size() - 1; j > i; j-- )
    {
      if( v[j] < v[j-1] )
      {
        unsigned long temp = v[j];
        v[j] = v[j-1];
        v[j-1] = temp;
      }
    }
  }
}

unsigned long solver( const vector<unsigned long>& motes, unsigned long initSize,
  unsigned long startIndex = 0 )
{
  if( initSize == 1 )
  {
    return motes.size() - startIndex;
  }
  unsigned long best = 0;
  unsigned long mySize = initSize;
  for( unsigned long i = startIndex; i < motes.size(); i++ )
  {
    if( motes[i] < mySize )
    {
      mySize += motes[i];
    }
    else
    {
      best = motes.size() - i;
      unsigned long x = 0;
      while( motes[i] >= mySize )
      {
        mySize = mySize * 2 - 1;
        x++;
      }
      if( x < best )
      {
        mySize += motes[i];
        unsigned long newBest = solver( motes, mySize, i+1 );
        if( newBest + x < best )
        {
          best = newBest + x;
        }
      }
      break;
    }
  }
  return best;
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
    unsigned long myMote, N;
    fin >> myMote >> N;
    vector<unsigned long> motes;
    motes.reserve(N);
    for( unsigned long j = 0; j < N; j++ )
    {
      unsigned long size;
      fin >> size;
      motes.push_back(size);
    }
    sort(motes);

    unsigned long answer = solver(motes, myMote);
    fout << answer;
  }

  fin.close();
  fout.close();
  return 0;
}