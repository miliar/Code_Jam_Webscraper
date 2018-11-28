
#include <iostream>
#include <string>
#include <cmath>
#include <sstream>
#include <stdlib.h>
#include <fstream>

using namespace std;

unsigned long long reverse(unsigned long long num)
{
    unsigned long long new_num = 0;
    while(num > 0)
    {
            new_num = new_num*10 + (num % 10);
            num = num/10;
    }
    return new_num;
}

bool is_palindrome(unsigned long long num)
{
  return (num == reverse(num));
}

unsigned long fair_and_square_count(unsigned long long low, unsigned long long high)
{
  unsigned long count = 0;
  for (unsigned long long i = ceil(sqrt(low)); i <= sqrt(high); i++) {
    if (is_palindrome(i) && is_palindrome(i * i)) {
      count ++;
    }
  }
  return count;
}

int main(int argc, char* argv[])
{
  ifstream inFile;
  inFile.open(argv[1]);
  if (!inFile) {
    cout<<"Unable to open : "<<argv[1]<<endl;
    return 0;
  }

  string strLine;
  getline(inFile, strLine);
  int TCCount = atoi(strLine.c_str());
  for(unsigned i = 0; i < TCCount; i++) {
    getline(inFile, strLine);
    istringstream iss(strLine);
    string sub;
    iss >> sub;
    unsigned long long low = atoi(sub.c_str());
    iss >> sub;
    unsigned long long high = atoi(sub.c_str());
    string result = "Case #";
    ostringstream convert1, convert2;
    convert1 << (i+1);
    result += convert1.str();
    result += ": ";
    unsigned long long count = fair_and_square_count(low, high);
    convert2 << count;
    result += convert2.str();
    cout<<result<<endl;
  }
  inFile.close();
  return 0;
}
