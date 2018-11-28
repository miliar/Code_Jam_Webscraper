#include <iostream>
#include <string>
#include <assert.h>
#include <algorithm>

using namespace std;

int flips(string pancakes)
{
  //cout << pancakes << endl;
  // Compress the string to just single + or -s
  {
    std::string newPancakes;
    char prev = 'A';
    for (int i=0; i<pancakes.size(); i++)
    {
      if ( (pancakes[i] == '+' || pancakes[i] == '-') && pancakes[i] != prev) {
        newPancakes.push_back(pancakes[i]);
        prev = pancakes[i];
      }
    }
    pancakes = newPancakes;
  }

  return 2*count(pancakes.begin(), pancakes.end(), '-') - (pancakes[0] == '-'? 1:0);
}

void tests()
{
  assert(flips("-") == 1);
  assert(flips("-+") == 1);
  assert(flips("+-") == 2);
  assert(flips("+++") == 0);
  assert(flips("--+-") == 3);


  assert(flips("-+++----++-+") == 5);
  assert(flips("+-+-+-+") == 6);
  assert(flips("+-+-+-+-") == 8);
  assert(flips("+-+-+-+-+") == 8);
}

int main()
{
  tests();
  //cout << "==============================" << endl;
  int n;
  cin >> n;
  string pancakes;
  getline(cin,pancakes);
  for (int i=0; i<n; i++)
  {
    getline(cin, pancakes);
    cout << "Case #" << i+1 << ": " <<  flips(pancakes) << endl;
  }
  return 0;
}
