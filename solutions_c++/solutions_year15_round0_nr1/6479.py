#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

int chose_friends(int max_shyness, string line);

int main(int argc, char *argv[])
{
  istream *in;
  ifstream infile;
  if(argc > 1)
  {
    infile.open(argv[1]);
    in = &infile;
  }
  else
  {
    in = &cin;
  }
  string line;
  int noOfCase = -1;
  int case_counter = 1;
  getline(*in, line);
  noOfCase = atoi(line.c_str());
  while (noOfCase > 0)
  {
    getline(*in,line, ' ');
    int max_shyness = atoi(line.c_str());

    getline(*in, line);
    int frnd_required = chose_friends(max_shyness, line);
    cout << "Case #" << case_counter << ": " << frnd_required << endl;
    case_counter++;
    noOfCase--;
  }
  if(infile.is_open())
    infile.close();
  return 0;
}

int chose_friends(int max_shyness, string line)
{
  int friends_counter = 0;
  int current_shyness = 0;
  for(int i =0; i < max_shyness, current_shyness < max_shyness; i++)
  {
    if(line[i] == '0' && current_shyness <= i )
    {
      friends_counter++;
      current_shyness++;
    }
    else
    {
      current_shyness += (line[i] - '0');
    }
  }
  return friends_counter;
}
