// codejam1

#include <iostream>

using namespace std;

typedef unsigned long long int ln;

bool isComplete(bool* found)
{
  for(int i =0; i < 10; i++)
    if(!found[i]) return false;
  return true;
}

int processNumber(ln number)
{
  bool found[10];
  for(int i =0; i < 10; i++) found[i] = false;
  while(true)
  {
    for(ln k = 1; ; k++)
    {
      int newNumber = k*number;
      while(newNumber != 0)
      {
        found[newNumber%10] = true;
        newNumber/= 10ll;
      }
      if(isComplete(found))
        return k*number;
    }
  }
}

int main()
{
  int size; ln number;
  cin >> size;
  for(int i =0 ; i < size; i++)
  {
    cin >> number;
    if(number != 0)
      cout << "Case #"<< i+1 << ": " << processNumber(number) << "\n";
    else cout << "Case #"<< i+1 << ": " << "INSOMNIA\n";
  }
}
