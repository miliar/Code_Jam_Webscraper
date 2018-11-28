#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
  int T;
  cin >> T;
  int caseNum = 1;
  
  while(caseNum <= T)
  {
    int A; 
    cin >> A;
    
    int N;
    cin >> N;
    vector<int> v (N,0);
    for(int i=0;i<N;i++)
    {
      cin >> v[i];
    }
    std::sort (v.begin(), v.end());
    
    vector<int> operations;
    if(A == 1)
    {
      operations.push_back(N);
    }
    else
    {
      int numAddOp = 0;
    
      for(int i=0;i<N;i++)
      {
        if(A > v[i])
        {
          A += v[i];
        }
        else
        {
          operations.push_back (numAddOp + (N-i));
          while(A <= v[i])
          {
            A += (A-1);
            //cout << "A=" << A << endl;
            numAddOp++;
          }
          A += v[i];
        }
      }
      
      if (numAddOp > 0)  operations.push_back (numAddOp);
    }
  
    if(operations.size() == 0)
    {
      cout << "Case #" << caseNum << ": 0" << endl;
    }
    else
    {
      std::sort (operations.begin(), operations.end());
      cout << "Case #" << caseNum << ": " << operations[0] << endl;
    }
    caseNum++;
  }

  return 0;
}
