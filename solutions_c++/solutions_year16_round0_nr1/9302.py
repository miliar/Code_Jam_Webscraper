#include <iostream>
#include <sstream>

using namespace std; 

bool arr[10] = {false};

bool isDone()
{
  for (int i=0; i<10; i++)
    if (arr[i] == false) 
      return false;
  return true;
}

void sheep(long long n, int ncase)
{
  // Reset the array
  for (int k=0; k<10; k++)
    arr[k] = false;
  cout << "Case #" << ncase << ": ";
  if (n == 0)
  {
    cout << "INSOMNIA" << endl;
    return;
  }

  long long i=0;
  while (!isDone())
  {
    i++;
    
    string str = to_string(i*n);
    for (int j=0; j<str.length(); j++)
      arr[str[j]-'0'] = true;
  }

  cout << i*n << endl;
}

int main()
{
  int n,j;
  cin >> n;
  for (int i=0; i<n; i++)
  {
    cin >> j;   
    sheep(j, i+1);
  }
}
