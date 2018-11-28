#include <iostream>
#include <vector>
#include <set>
#include <fstream>
using namespace std;

int main()
{
 ifstream fin;
 fin.open("A-small-attempt2.in");
 ofstream fout;
 fout.open("A-small.out");
 set<int> valid;
 vector<int> valid2;
 vector< vector<int> > cards;
 cards.resize(4);
 for(int i = 0; i < 4; ++i)
 {
  cards[i].resize(4);
 }
 int cases;
 fin >> cases;
 for(int z = 0; z < cases; ++z)
 {
  valid2.resize(0);
  int guess1, guess2;
  fin >> guess1;
  --guess1;
  for(int i = 0; i < 4; ++i)
  {
   for(int j = 0; j < 4; ++j)
   {
    fin >> cards[i][j];
   }
  }
  for(int i = 0; i < 4; ++i)
  {
   valid.insert(cards[guess1][i]);
  }
  fin >> guess2;
  --guess2;
  for(int i = 0; i < 4; ++i)
  {
   for(int j = 0; j < 4; ++j)
   {
    fin >> cards[i][j];
   }
  }
  for(int i = 0; i < 4; ++i)
  {
   if(valid.count(cards[guess2][i]) != 0)
   {
    valid2.push_back(cards[guess2][i]);
   }
  }

  fout << "Case #" << (z + 1) << ": ";

  if(valid2.size() == 1)
  {
   fout << valid2[0] << endl;
  }
  else if(valid2.size() == 0)
  {
   fout << "Volunteer cheated!\n";
  }
  else
  {
   fout << "Bad magician!\n";
  }
  valid.clear();
  valid2.clear();
 }

 return (0);
}
