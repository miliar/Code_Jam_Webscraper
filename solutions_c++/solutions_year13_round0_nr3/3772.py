#include <iostream>
#include <string>
#include <sstream>

using namespace std;

bool estPalindrome (long long nombre)
{
  stringstream stream;
  stream << nombre;

  string chaine = stream.str();

  for (size_t i = 0; i < (chaine.size() / 2); i++) {
    if (chaine[i] != chaine[chaine.size() - i - 1]) {
      return false;
    }
  }

  return true;
}

int nbPalindromesCarres(long long borneInf, long long borneSup)
{
  int resultat = 0;
  long long nombre = 1;

  while (nombre * nombre <= borneSup) {
    if (estPalindrome(nombre) && estPalindrome(nombre * nombre) &&
	nombre * nombre >= borneInf && nombre * nombre <= borneSup) {
      resultat++;
    }

    nombre++;
  }

  return resultat;
}

int main(int argc, char** argv)
{
  int nbTests;

  cin >> nbTests;

  for(int i = 0; i < nbTests; i++){
    long long borneInf, borneSup;
    cin >> borneInf >> borneSup;

    cout << "Case #" << i + 1 << ": ";
    cout << nbPalindromesCarres(borneInf, borneSup);
    cout << endl;
  }

  return 0;
}
