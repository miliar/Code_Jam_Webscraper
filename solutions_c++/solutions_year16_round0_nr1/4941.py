#include <iostream>
#include <typeinfo>
#include <string>
#include <unistd.h>
#include <array>
#include <vector>
#include <sstream>

using namespace std;

string solveCase(uint64_t start);

int main()
{
   int count;
   cin >> count;

   for (int i = 0; i<count; ++i) {
      uint64_t start;
      cin >> start;
      string result = solveCase(start);
      cout << "Case #" << (i + 1) << ": " << result << endl;
   }

   return 0;
}

void updateSeen(vector<bool> &seen, uint64_t start)
{
   while (start != 0) {
      seen[start % 10] = true;
      start /= 10;
   }
}

bool isEveryDigitSeen(vector<bool> &seen)
{
   for (bool iter : seen)
      if (iter == false)
         return false;
   return true;
}

//string to_string(uint64_t num)
//{
//   ostringstream os;
//   os << num;
//   return os.str();
//}

string solveCase(uint64_t start)
{
   if (start == 0)
      return "INSOMNIA";

   vector<bool> seen(10, false);
   uint64_t value = start;

   for (uint32_t i = 2; value<=numeric_limits<uint64_t>::max() / 2; value = start * (i++)) {
      updateSeen(seen, value);
      if (isEveryDigitSeen(seen))
         return to_string(value);
   }

   return "INSOMNIA";
}
