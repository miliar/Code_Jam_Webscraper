//============================================================================
// Name        : Contest_MagicTrick.cpp
// Author      : richard
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <set>

using namespace std;


class MagicStore
{
public:
  static const int CardRow = 4;
  static const int CardColumn = 4;
public:
  MagicStore(void):
    mCardPre_1(CardRow),
    mCardPre_2(CardColumn)
  {
      vector< vector<int > >::iterator it = mCardPre_1.begin();
      for (it;it!=mCardPre_1.end();it++)
        {
            it->resize(CardColumn);
        }
      it = mCardPre_2.begin();
      for (it;it!=mCardPre_2.end();it++)
        {
          it->resize(CardColumn);
        }
  }
  static MagicStore * readAndformat(void);
public:
  vector< vector<int> > mCardPre_1;
  vector< vector<int> > mCardPre_2;
  int mRow_1;
  int mRow_2;
};

MagicStore * MagicStore::readAndformat(void)
{
  MagicStore * magic = new MagicStore();

  cin>>(magic->mRow_1);
  int i,j;
  for (i=0;i<magic->mCardPre_1.size();i++)
    {
      for (j=0;j<magic->mCardPre_1[i].size();j++)
        {
          cin>>magic->mCardPre_1[i][j];

        }
    }
  cin>>(magic->mRow_2);
  for (i=0;i<magic->mCardPre_2.size();i++)
    {
      for (j=0;j<magic->mCardPre_2[i].size();j++)
        {
          cin>>magic->mCardPre_2[i][j];

        }
    }
  return magic;
}



int guessCard(MagicStore * magic)
{
  set<int>firstCards;
  int i;
  int row = magic->mRow_1-1;
  for (i=0;i<magic->mCardPre_1[row].size();i++)
    {
      firstCards.insert(magic->mCardPre_1[row][i]);

    }
  row = magic->mRow_2-1;
  int hit = 0;
  int card = 0;
  for (i=0;i<magic->mCardPre_2[row].size();i++)
    {
      if (firstCards.find(magic->mCardPre_2[row][i])!=firstCards.end())
        {
          hit++;
          card =magic->mCardPre_2[row][i];
        }
    }
  if (hit==1)
    {
      return card;
    }
  else if (hit>1)
    {
      return -1;
    }
  else
    {
      return 0;
    }
}

void outPutGuess(int time,int result)
{
   cout<<"Case #"<<time<<": ";
  switch(result)
  {
  case 0:
    cout<<"Volunteer cheated!";
    break;
  case -1:
    cout<<"Bad magician!";
    break;
  default:
    cout<<result;
  }
   cout<<endl;
}
int main()
{
    int times;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>times;
    int i;
    int ret;
    for (i=0;i<times;i++)
      {
        MagicStore *magic =MagicStore::readAndformat();
        ret = guessCard(magic);
        outPutGuess(i+1,ret);
        delete magic;

      }


	return 0;
}
