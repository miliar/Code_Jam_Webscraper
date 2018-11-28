#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int min_ancestors(int P, int Q)
{
  if ( ((Q)&((Q)-1)) != 0)  return -1; // not possible
  
  double tmp = (P*1.0)/Q;
  
  int level = 1;
  for (level = 1; level<=40; level++) {
    if (pow(0.5, level) <= tmp) {
      break;
    }
  }

  return level;
}

int main()
{
  int n_cases;
  ifstream file("A.in", ios::in);

  file >> n_cases;
  
  for (int case_no=1; case_no <= n_cases; case_no++) {
    int P,Q;
    string s;
    file >> s;

    P = atoi(s.substr(0, s.find('/')).c_str());
    Q = atoi(s.substr(s.find('/')+1 ).c_str());

    int retval = min_ancestors(P, Q);
  
    if (retval == -1) {
      cout << "Case #" << case_no << ": impossible";
    } else {
      cout << "Case #" << case_no << ": " << retval;
    }
    cout <<endl;
  }
  return 0;
}
