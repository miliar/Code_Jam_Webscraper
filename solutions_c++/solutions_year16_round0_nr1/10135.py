#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <map>

using namespace std;

int computeNumber(int n) 
{
   map<int, bool> m;
   int u = 0;

   for (; ;) {
     int x = u + n;
     u = x;

     while (x > 0) 
     {
       int y = x % 10;
       map<int, bool>::iterator it = m.find(y);
       if (it == m.end()) 
       {
          m.insert(pair<int, bool>(y,true));
          if (m.size() == 10) 
          {
              return u;
          }
       }
       x = x / 10;
     }
     factor++;
   }
}

int main(int argc, char **argv) 
{
 ifstream myfile(argv[1]);
 string line;
 bool first = false;
 int T, n;
 int caseNumber = 0;
 while (getline(myfile, line))
 {
   istringstream iss(line);
   if (first == false) {
     iss >> T;
     first = true;
   }
   else 
   {
     iss >> n;
     if (n == 0) {
         cout << "Case #" << caseNumber << ": INSOMNIA" << endl;
     } 
     else 
     {
         int lastNumber = computeNumber(n);
         cout << "Case #" << caseNumber << ": " << lastNumber << endl;
     }
   }
   caseNumber++;
  }
}
