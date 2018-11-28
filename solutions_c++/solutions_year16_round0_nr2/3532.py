// codejam2

#include <iostream>
#include <string>
using namespace std;

int recurse(string& linha, int max, int mode)
{
  if(max == 0)
  {
    if(linha[max] == '+' && mode == 1)
      return 0;
    else if(linha[max] == '-' && mode == -1)
      return 0;
    return 1;
  }
  if(linha[max] == '+')
  {
    if(mode == 1)
      return recurse(linha,max-1,mode);
    else
      return recurse(linha,max-1, mode*(-1)) + 1;
  }
  else
  {
    if(mode == -1)
      return recurse(linha,max-1,mode);
    else
      return recurse(linha,max-1, mode*(-1)) + 1;
  }
}

int processLinha(string& linha)
{
  return recurse(linha, linha.size()-1, 1);
}

int main()
{
  int size;
  string linha;
  cin >> size;
  for(int i = 0; i < size; i++)
  {
    cin >> linha;
    cout << "Case #" << i+1 << ": " << processLinha(linha) << "\n";
  }
}
