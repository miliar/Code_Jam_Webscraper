#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string returnVal;

bool breakString(string number, string remove)
{

  bool good = true;
  string temp = number;
  while(good)
  {
    if(number.size() == 0)
      break;
    //cout << "Run" << endl;
    bool good2 = true;
    for(int j = 0; j < remove.size() && good2; j++)
    {

      for(int k = 0; k < temp.size(); k++)
      {
        if(temp.at(k) == remove.at(j))
        {
          //cout << temp << endl;
          //cout << temp.at(k) << endl;
          //cout << temp.size() << endl;
          temp.erase(temp.begin()+k);
          //cout << temp << endl<<endl;
          k--;
          break;
        }
        if(k == temp.size() - 1)
        {
          good2 = false;
        }
      }
    }
    if(!good2)
    {
      break;
    }else
    {
      number = temp;
      returnVal = temp;
      return true;
      //cout << i;
      //cout << number << endl;
    }
  }
  return false;
}

bool stop;
string lookUp[10] = {"0","1","2","3","4","5","6","7","8","9"};
void recurse(string a, string sol)
{
  if(a == "")
  {
    cout << sol << endl;
    stop = true;
    return;
  }
  string data[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
  for(int i = 0; i < 10 && !stop; i++)
  {
    if(breakString(a, data[i]))
    {
      recurse(returnVal, sol + lookUp[i]);
    }
  }
}

int main(int argc, char* argv[])
{
  int casses;
  cin >> casses;
  for(int caseNum = 1; caseNum <= casses; caseNum++)
  {
    stop = false;

    cout << "Case #" << caseNum << ":" << " ";
    string number;
    cin >> number;
    recurse(number, "");
    //breakString(number);
    //cout << "Done" << endl;
  }
  return 0;
}
