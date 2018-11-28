#include <iostream>
#include <typeinfo>
#include <string>
#include <unistd.h>
#include <array>
#include <vector>
#include <sstream>

using namespace std;

uint32_t solveCase(string &pancakes);

int main()
{
   int count;
   cin >> count;

   for (int i = 0; i<count; ++i) {
      string pancakes;
      cin >> pancakes;
      uint32_t result = solveCase(pancakes);
      cout << "Case #" << (i + 1) << ": " << result << endl;
   }

   return 0;
}

bool arePancakesGood(const string &pancakes) // Stupid question .. pancakes are awesome :))
{
   for (int i = 0; i<pancakes.length(); ++i) {
      if (pancakes[i] == '-')
         return false;
   }
   return true;
}

int getFlipPosition(const string &pancakes)
{
   char first = pancakes[0];
   for (int i = 1; i<pancakes.length(); i++) {
      if (pancakes[i] != first)
         return i - 1;
   }
   return pancakes.length() - 1;
}

void doFlip(string &pancakes, int badPancake)
{
   // reverse and invert range [0; badPancake]
   for (int i = 0; i<=badPancake / 2; ++i) {
      char buffer = pancakes[i];
      pancakes[i] = pancakes[badPancake - i] == '-' ? '+' : '-';
      pancakes[badPancake - i] = buffer == '-' ? '+' : '-';
   }
}

uint32_t solveCase(string &pancakes)
{
   uint32_t operations = 0;
   while (!arePancakesGood(pancakes)) {
      int firstBadPancake = getFlipPosition(pancakes);
      doFlip(pancakes, firstBadPancake);
      operations++;
   }

   return operations;
}
