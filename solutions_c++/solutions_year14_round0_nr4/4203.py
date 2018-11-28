#include <cstdio>
#include <algorithm>
#include <deque>

using namespace std;

int scoreStrategie(deque<double> poidsA, deque<double> poidsB)
{
  int nbtours = poidsA.size();
  int scoreA = 0;
  for(int tour = 0; tour < nbtours; tour++)
  {
    
    if(poidsA.front() < poidsB.front())
    {
      poidsA.pop_front(); 
      poidsB.pop_back();
    }
    else
    {
      poidsA.pop_front();
      poidsB.pop_front();
      scoreA++;
    }


  }
  return scoreA;
}

int main()
{
  int nbtests;
  scanf("%d",&nbtests);
  for(int t = 1; t <= nbtests; t++)
  {
    int nbpoids;
    scanf("%d", &nbpoids);
    deque<double> poidsA(nbpoids);
    deque<double> poidsB(nbpoids);
    for(int i = 0; i < nbpoids; i++)
    {
      scanf("%lf", &poidsA[i]);
    }
    for(int i = 0; i < nbpoids; i++)
    {
      scanf("%lf", &poidsB[i]);
    }
    sort(poidsA.begin(),poidsA.end());
    sort(poidsB.begin(),poidsB.end());
    int scoreAD = scoreStrategie(poidsA, poidsB);
    int scoreAW = poidsA.size() - scoreStrategie(poidsB, poidsA);
    printf("Case #%d: %d %d\n",t,scoreAD,scoreAW);
  }
  return 0;
}

