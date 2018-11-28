
#include<iostream>
#include<sstream>
#include<string>
#include<map>
#include<vector>
#include<cmath>


// 1, 4, 9, 121, 484

int main() 
{
  using namespace std;

  int T = 0;
  cin >> T;

  std::string str;
  getline(cin, str);

  int i = 0;
  for (i=1;i<=T;i++) 
  {
    int A,B;
    cin >> A;
    cin >> B;

    int found = 0;
    if (A <= 1 && B >= 1) found++;
    if (A <= 4 && B >= 4) found++;
    if (A <= 9 && B >= 9) found++;
    if (A <= 121 && B >= 121) found++;
    if (A <= 484 && B >= 484) found++;

    cout << "Case #" << i << ": " << found << endl;
  }
}

