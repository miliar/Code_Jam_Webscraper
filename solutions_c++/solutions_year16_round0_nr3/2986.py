// googlejam3
#include <iostream>
#include <string>
#include <vector>
using namespace std;

typedef long long int lli;
const lli MAX = 10001000;

vector<lli> primos{2,3};

void geraprimos()
{
  for(lli i = 4; i < MAX; i++)
  {
    lli j;
    for(j = 0; j < primos.size() && primos[j]*primos[j] < i; j++)
      if(i % primos[j] == 0)
        break;
    if(i % primos[j] != 0) primos.push_back(i);
  }
}

lli converte(string num, lli base)
{
  lli aux = 1;
  lli value = 0;
  for(int i = num.size()-1; i >= 0; i--)
  {
    value += (num[i]-'0')*aux;
    aux *= base;
  }
  return value;
}

int naoEhPrimo(lli value)
{
  for(int i = 0; i < primos.size() && primos[i]*primos[i] <= value; i++)
  {
    if(value % primos[i] == 0) return primos[i];
  }
  return -1;
}

void testa(string a)
{
  static int cont = 0;
  if (cont == 50)return;
  lli divisores[10];
  for(int i = 2; i <= 10; i++)
  {
    lli value = converte(a, i);
    lli divisor = naoEhPrimo(value);
    if(divisor == -1)
    {
      return;
    }
    else divisores[i] = divisor;
  }
  cont++;
  cout << a;
  for(int i = 2; i <= 10; i++)
    cout << " " << divisores[i];
  cout << "\n";
}

void recursivo(string a, int pos)
{
  if(pos == 14)
  {
    testa(a);
    return;
  }
  else
  {
    recursivo(a, pos+1);
    a[pos] = '1';
    recursivo(a, pos+1);
  }
}


int main()
{
  geraprimos();
  cout << "Case #1:\n";
  recursivo("1000000000000001", 0);
}
