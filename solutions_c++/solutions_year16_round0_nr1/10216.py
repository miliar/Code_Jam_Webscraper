#include <iostream>
using namespace std;

int main()
{
  // Program Constants
  const int INSOMNIA = 0;
  const int TERM = 0;
  const int NUM_SIZE = 10;
  const int DIVISOR = 10;
  
  // Input Variables
  int numCases;
  int startNum;
  
  // Program Variables
  int caseNum = 0;
  int multiplier = 0;
  int temp;
  int modNum;
  int oldNum;
  
  bool isDone;
  
  cin >> numCases;
  
  // Go Through Each Case
  for (int k = 0; k < numCases; k++)
  {
    bool nums[NUM_SIZE] = {false, false, false, false, false, false, false,
                           false, false, false};
                           
    isDone = false;
    
    cin >> startNum;
    
    oldNum = startNum;
    
    // Check For Insomnia
    if (startNum == INSOMNIA)
    {
      caseNum++;
      
      cout << "Case #" << caseNum << ": INSOMNIA" << endl;
    
      continue;
    }
    
    // Check For All Digits Found
    while (!isDone)
    {
      startNum = oldNum;
      
      multiplier++;
      startNum *= multiplier;
      
      temp = startNum;
      
      // Go Through Each Digit
      while (temp != TERM)
      { 
        modNum = temp % DIVISOR;
    
        nums[modNum] = true;
      
        temp /= DIVISOR;
      }
      
      // Check Every Index Of nums
      isDone = true;
      
      for (int j = 0; j < NUM_SIZE; j++)
      { 
        if (nums[j] == false)
        {
          isDone = false;
          break;
        }
      }
    }
    
    caseNum++;
    
    cout << "Case #" << caseNum << ": " << startNum << endl;
    
    multiplier = 0;
  }
  
  return 0;
}