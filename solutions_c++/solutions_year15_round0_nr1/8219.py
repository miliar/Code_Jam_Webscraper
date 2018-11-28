#include <iostream>
#include <fstream>
#include <vector>
#include <cstring>
#include <map>

using namespace std;


int number(string a)
{
  int friends = 0;
  int standing = a[0] - '0';
  for (int i = 1; i < a.length(); i++)
  {
    int tf = i - standing;
  //  cout << "tf " << tf <<  "  friends  " << friends << "  standing  " << standing << endl;
    if (tf > 0)
    {
      friends += tf;
      standing += tf;
    }
    standing += a[i] - '0';
  }
  return friends;
}

int main()
{
  ifstream read;
  ofstream write;
  read.open("A-large.in");
  write.open("output.txt");
  if (!read)
    cout << "ERROR 404. File not found" << endl;
  string T;
  read >> T;
  cout << "T " << T << endl;
  int limit = atoi(T.c_str());
  int counter = 1;
  while (counter <= limit)
  {
    string in;
    read >> in;
 //   cout << "pehla in " << in << endl;
    read >> in;
 //   cout << "in " << in << endl;
    int ans = number(in);
    write << "Case #" << counter << ": " << ans << "\n";
    counter++;
 //   cout << "ans " << ans << "  counter " << counter << endl;
  }
  return 0;
}
