//============================================================================
// Name        : DeceitWar.cpp
// Author      : richard
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class War
{
public:
  War(int nBlocks):
    mBlocks(nBlocks),
    mNaomi(nBlocks),
    mKen(nBlocks)
  {
  }
  void readBlocks(void);
  int playWar(void);
  int playDeceitWar(void);
private:
  int mBlocks;
  vector<float> mNaomi;
  vector<float> mKen;
};
int War::playDeceitWar(void)
{
  vector<float> tmp(mNaomi);
  mNaomi = mKen;
  mKen = tmp;
  return mBlocks-playWar();
}
int War::playWar(void)
{
  vector<float>cpNaomi(mNaomi);
  vector<float>cpKen(mKen);
  int kenWin=0;
  int naomiWin=0;
  float massNaomi;
  float massKen;
  bool kenwin = false;
  vector<float>::iterator iter;
  int i;
  for (i=0;i<mBlocks;i++)
    {
      massNaomi = cpNaomi.front();
      iter=cpKen.begin();
      for (;iter!=cpKen.end();iter++)
        {
          massKen = (*iter);
          if (massKen>massNaomi)
            {
              kenWin++;
              kenwin = true;
              cpKen.erase(iter);
              break;
            }
        }
      if (kenwin)
        {
          kenwin = false;
          cpNaomi.erase(cpNaomi.begin());
        }
      else
        {
          break;
        }

    }
  naomiWin = mBlocks-kenWin;

  return naomiWin;
}
void War::readBlocks(void)
{
  int i=0;
  for (i=0;i<mBlocks;i++)
    {
      cin>>mNaomi[i];
    }
  for (i=0;i<mBlocks;i++)
    {
      cin>>mKen[i];
    }
  sort(mNaomi.begin(),mNaomi.end());
  sort(mKen.begin(),mKen.end());
}

void outPut(int time,int naomiWarWin,int naomiDeceitWin )
{
  cout<<"Case #"<<time<<": "<<naomiDeceitWin<<" "<<naomiWarWin<<endl;
}

int main()
{
  int times;
  int i;
  int nBlocks;
  //freopen("large.txt","r",stdin);
  //freopen("outputlarge.txt","w",stdout);
  cin>>times;
  int naomiWarWins;
  int naomiDeceitWins;
  for (i=0;i<times;i++)
    {
      cin>>nBlocks;
      War war(nBlocks);
      war.readBlocks();
      naomiWarWins = war.playWar();
      naomiDeceitWins = war.playDeceitWar();
      outPut(i+1,naomiWarWins,naomiDeceitWins);
    }

	return 0;
}
