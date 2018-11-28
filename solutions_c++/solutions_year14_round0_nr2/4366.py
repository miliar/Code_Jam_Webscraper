#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>


using namespace std;


int main()
{
  int nbtestcases;
  scanf("%d", &nbtestcases);

  for(int t = 1; t <= nbtestcases; t++)
  {
    double c,f,x;
    scanf("%lf%lf%lf",&c,&f,&x);
    double seuil = (x*f -2.*c)/(c*f) - 1.;
    int nbfermes = ceil(seuil);
    nbfermes = max(0,nbfermes);
    double reponse = x/(2. + double(nbfermes) * f);
    double temp = 0;
    for(int i = nbfermes - 1; i >= 0; i--)
    {
      temp += 1/(2. + double(i)*f);
    } 
    temp *= c;
    reponse += temp;
    printf("Case #%d: %.7lf\n",t,reponse);
  }
  return 0;
}
