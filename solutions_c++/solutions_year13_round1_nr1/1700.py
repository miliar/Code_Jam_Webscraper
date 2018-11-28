#include <iostream>
#include <string>

using namespace std;

unsigned long long aireCercle (unsigned long long rayon)
{
  return rayon * rayon;
}

unsigned long long nbCercles (unsigned long long rayonInitial,unsigned long long peinture)
{
  unsigned long long rayonMin, rayonMax, resultat;

  rayonMin = rayonInitial;
  rayonMax = rayonInitial + 1;
  resultat = 0;

  while (aireCercle(rayonMax) - aireCercle(rayonMin) <= peinture) {
    resultat++;
    peinture -= aireCercle(rayonMax)  - aireCercle(rayonMin);

    // cout << " " << aireCercle(rayonMax) << " " << aireCercle(rayonMin) << " " << peinture << endl;

    rayonMin += 2;
    rayonMax += 2;
  }

  return resultat;
}

int main(int argc, char** argv)
{
  int nbTests;

  cin >> nbTests;

  for(int i = 0; i < nbTests; i++){
    unsigned long long rayonInitial, peinture;

    cin >> rayonInitial >> peinture;

    cout << "Case #" << i + 1 << ": " << nbCercles(rayonInitial, peinture) << endl;
  }

  return 0;
}
