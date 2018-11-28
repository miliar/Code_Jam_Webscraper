#include <iostream>
#include <list>

using namespace std;

int deceitfulWar(list<double> naomi, list<double> ken)
{
  int points=0;

  list<double>::reverse_iterator itNaomi, itKen;

  for(itNaomi = naomi.rbegin(); itNaomi != naomi.rend(); itNaomi++)
  {
    for(itKen = ken.rbegin(); itKen != ken.rend(); itKen++)
    {
      if(*itNaomi > *itKen)
      {
        points++;
        ken.erase(--(itKen.base()));
        break;
      }
    }
  }

  return points;
}

int war(list<double> naomi, list<double> ken)
{
  int points=0;

  list<double>::reverse_iterator itNaomi;

  for(itNaomi = naomi.rbegin(); itNaomi != naomi.rend(); itNaomi++)
  {
    if(*itNaomi > ken.back())
    {
      points++;
      ken.pop_front();
    }
    else
      ken.pop_back();
  }

  return points;
}

int main()
{
  int n;
  cin >> n;

  for(int i=0; i<n; i++)
  {
    int qtd;

    list<double> naomi;
    list<double> ken;

    double weight;

    cin >> qtd;

    for(int x=0; x<qtd; x++)
    {
      cin >> weight;
      naomi.push_back(weight);
    }

    for(int x=0; x<qtd; x++)
    {
      cin >> weight;
      ken.push_back(weight);
    }

    naomi.sort();
    ken.sort();

    int pointsDeceitful = deceitfulWar(naomi, ken);
    int pointsNormal = war(naomi, ken);

    cout << "Case #" << i+1 << ": " << pointsDeceitful << " " << pointsNormal << endl;
  }

  return 0;
}
