
#include <iostream>
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


  deque<char> d;
  
  d.push_back(word[0]);
  for (int widx = 1; widx < word.length(); widx++)
  {
    if (word[widx] >= d.front())
      d.push_front(word[widx]);
    else
      d.push_back(word[widx]);
  }
  
  cout << "Case #" << c << ": ";
  while (!d.empty())
  {
    cout << d.front(); d.pop_front();
  }
  cout << endl;

}


int main()
{
  int numcases;
  cin >> numcases;
  
  for (int c = 0; c < numcases; c++)
    processCase(c+1);
}

