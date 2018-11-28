
#include <iostream>
#include <sstream>
#include <cassert>
#include <vector>
#include <set>
#include <queue>
#include <deque>
#include <map>
#include <algorithm>


using namespace std;


void processCase(int c)
{
  string word;
  cin >> word;


  map<char,int> h;
    
  for (int widx = 0; widx < word.length(); widx++)
  {
    if (h.count(word[widx]) > 0)
      h[word[widx]]++;
    else
      h.insert(pair<char,int>(word[widx],1));
  }
  
  char keyletters[] = {'Z','X','W','U','G','R','F','V','O','N'};
  int  keyvalues [] = { 0,  6 , 2 , 4 , 8 , 3 , 5 , 7 , 1 , 9 };
  map<char,string> searchmap = { {'Z', "ZERO"}, {'O', "ONE"}, {'W', "TWO"}, {'R', "THREE"}, {'U', "FOUR"}, {'F', "FIVE"}, {'X', "SIX"}, {'V', "SEVEN"}, {'G',"EIGHT"}, {'N',"NINE"}};
  
  
  stringstream ss;
  
  for (int i = 0; i < 10; i++)
  {
    char key = keyletters[i];
    cerr << key << ": " << h[key] << endl;
    while (h[key] > 0)
    {
      ss << keyvalues[i];
      //cerr << i << endl;
      for (auto c : searchmap[key])
      {
         //cerr << "h(" << c << ")=" << h[c] << endl;
         h[c]--;
         assert(h[c]>=0);
         //cerr << "h(" << c << ")=" << h[c] << endl;
      }
    }
  }
  
  string tmp = ss.str();
  sort(tmp.begin(),tmp.end());
  
  cout << "Case #" << c << ": " << tmp << endl;
}


int main()
{
  int numcases;
  cin >> numcases;
  
  for (int c = 0; c < numcases; c++)
    processCase(c+1);
}

