#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cstddef>

using namespace std;

int main()
{
  unsigned long long Test;
  cin >> Test;
  for(unsigned long long tt=1 ; tt<=Test ; tt++)
  {
    string Input;
    cin >> Input;
    char Happy = '+';
    char Unhappy = '-';
    bool IsSolved = false;
    unsigned long long Counter = 0;
  //  cout << "Starting" << endl;
    for(; ; Counter++)
    {
//      cout << "Counter = " << Counter << endl;
      //cout << "Input = " << Input << endl;
      if (Input.find(Unhappy) == std::string::npos && (IsSolved = true)) break;
      size_t LastHappy = Input.rfind(Unhappy);
      Input = Input.substr(0,LastHappy + 1);
      //cout << "Stripped Input = " << Input << endl;
      if(Input[0] == Happy)
      {
        int jj;
        for(jj = 0 ; Input[jj] == Happy; jj++)
          Input[jj] = Unhappy;
        Counter++;
      //  cout << "Counter = " << Counter << endl;
    //    cout << "Input = " << Input << endl;
      }
      reverse(Input.begin(),Input.end());
      for(int jj = 0 ; jj < Input.size() ; jj++)
        Input[jj] = (Input[jj] == Unhappy ? Happy : Unhappy);
  //    cout << "Input = " << Input << endl;
    }
//    cout << "Solved Counter = " << Counter << endl;
    cout << "Case #"<< tt << ": " << Counter << endl;
  }
  return 0;
}
