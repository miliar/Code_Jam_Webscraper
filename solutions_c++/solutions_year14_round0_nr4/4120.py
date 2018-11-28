#include "DeceitfulWar.h"
#include <iomanip>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
struct Comp
{
      Comp(float v) : m_v(v) { }

          bool operator()(const float v) const
                {
                          return v > m_v;
                }

              float m_v;
};


int actual_game( vector<float> naomi_blocks, vector<float> kens_blocks)
{
  float naomi_choice;
  float kens_choice;
  int naomi_wins = 0;

  std::sort( naomi_blocks.begin(), naomi_blocks.end() );
  std::sort( kens_blocks.begin(), kens_blocks.end() );
  
  cout << naomi_blocks.size() << endl;

  while( naomi_blocks.begin() != naomi_blocks.end() )
  {
    cout << "entered loop" << endl;

    naomi_choice = naomi_blocks.front();
    naomi_blocks.erase(naomi_blocks.begin());

    vector<float>::iterator it = std::find_if(kens_blocks.begin(), kens_blocks.end(), Comp(naomi_choice));
    if ( it == kens_blocks.end() )
      it = kens_blocks.begin();

    kens_choice = *it;
    kens_blocks.erase(it);

    cout << "kens choice " << kens_choice << " naomi choice " << naomi_choice << endl;
    
    if( naomi_choice > kens_choice) ++naomi_wins;
  }

  return naomi_wins;

}

int deceitful_game( vector<float> naomi_blocks, vector<float> kens_blocks)
{

  float naomi_choice, naomi_tells;
  float kens_choice;
  int naomi_wins = 0;

  std::sort( naomi_blocks.begin(), naomi_blocks.end() );
  std::sort( kens_blocks.begin(), kens_blocks.end() );
  
  cout << naomi_blocks.size() << endl;

  while( naomi_blocks.begin() != naomi_blocks.end() )
  {
    cout << "entered loop" << endl;

    vector<float>::iterator it = std::find_if(naomi_blocks.begin(), naomi_blocks.end(), Comp(kens_blocks.front()));

    //naomi_choice = naomi_blocks.front();
    //naomi_blocks.erase(naomi_blocks.begin());
    
    if( it != naomi_blocks.end() )
    {
      naomi_choice = *it;
      naomi_blocks.erase(it);
      naomi_tells = kens_blocks.back() + .000001;
    }
    else
    {
      naomi_choice = naomi_blocks.front();
      naomi_blocks.erase(naomi_blocks.begin());
      naomi_tells = naomi_choice;
    }

    it = std::find_if(kens_blocks.begin(), kens_blocks.end(), Comp(naomi_tells));
    if ( it == kens_blocks.end() )
      it = kens_blocks.begin();

    kens_choice = *it;
    kens_blocks.erase(it);

    cout << "kens choice " << kens_choice << " naomi choice " << naomi_choice << endl;
    
    if( naomi_choice > kens_choice) ++naomi_wins;
  }

  return naomi_wins;

}

template <typename T>
int greater_than( T* first, T* second, int size )
{
  int count = 0;

  for( int i = 0; i < size; ++i )
  {
    if( *(first + i) > *(second + i) )
      ++count;
  }

  return count;
}

DeceitfulWar::DeceitfulWar( ifstream& infile )
{
  string line = "";
  infile >> _testcases;
  _outfile.open("output_deceitful_war.txt");

  for( int i = 1; i <= _testcases; ++i )
  {
    _outfile << "Case #" << i << ": ";
    int size;
    infile >> size;
    vector<float> kens_blocks, naomi_blocks;
    naomi_blocks.reserve(size);
    kens_blocks.reserve(size);
    vector<float>::iterator  naomi = naomi_blocks.begin(), ken = kens_blocks.begin();
    float num;

    for( int i = 0; i < size; ++i)
    {
      infile >> num;
      naomi_blocks.push_back(num);
    }

    for( int i = 0; i < size; ++i)
    {
      infile >> num;
      kens_blocks.push_back(num);
    }

    int deceitful = deceitful_game( naomi_blocks, kens_blocks );
    int actual = actual_game( naomi_blocks, kens_blocks );

    _outfile << deceitful << " " << actual;

    _outfile << "\n";
  }
}

DeceitfulWar::~DeceitfulWar()
{
  _outfile.close();
}
