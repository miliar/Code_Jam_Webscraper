#include <iostream>
#include <cstdlib>
#include <stdio.h>


using namespace std;

double obj,farm_prod,farm_price;



int main() {
  cout.precision(14);
  int i,j,k;
  int nb_cas,cas;
  int nb_farm;
  double time;
  double result;
  double prod_local;
  double result_temp;
  double ex_time;
  cin >> nb_cas;
  for(cas=1;cas<=nb_cas;cas++) {
    cin >> farm_price >> farm_prod >> obj;
    nb_farm=0;
    result=obj/2.0;
    ex_time=0.0;
    while(1) {
      nb_farm++;
      time=0;
      prod_local=2.0;
      time=ex_time+farm_price/(2.0+farm_prod*(nb_farm-1));
      ex_time=time;
      result_temp = time + obj/(2.0+farm_prod*nb_farm);
      if(result_temp > result)
	break;
      result=result_temp;
    }
    cout << "Case #" << cas << ": ";
    printf("%.7lf\n",result);
  }
}
