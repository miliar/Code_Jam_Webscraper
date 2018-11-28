#include <algorithm>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <stdio.h>

//#define DEBUG

using namespace std;

int main(int argc, char** argv)
{
  int case_total;
  int case_num;
  
  int max_shyness;
  int cur_shyness;
  int audience_sum;     // current sum of audience members
  int audience_plant;   // num planted audience members
  
  int audience[1001];
  
  cin >> case_total;
  
  // Input
  for (case_num = 1; case_num <= case_total; case_num++)
  {
    audience_sum = 0;
    audience_plant = 0;
    
    cin >> max_shyness;
    cin.ignore();
    
    // Input
    for (cur_shyness = 0; cur_shyness <= max_shyness; cur_shyness++)
    {
      audience[cur_shyness] = (int) (cin.get() - '0');
    }
    
#ifdef DEBUG
    cerr << max_shyness << ' ';
    for (int i = 0; i <= max_shyness; i++)
    {
      cerr << audience[i];
    }
    cerr << endl;
#endif
    
    // Processing
    for (cur_shyness = 0; cur_shyness <= max_shyness; cur_shyness++)
    {
      if (audience_sum + audience_plant < cur_shyness)
      {
        audience_plant += cur_shyness - (audience_sum + audience_plant);
      }
      audience_sum += audience[cur_shyness];
    }
    
    // Output
    cout << "Case #" << case_num << ": " << audience_plant << endl;
  }
  
  
  return 0;
}

