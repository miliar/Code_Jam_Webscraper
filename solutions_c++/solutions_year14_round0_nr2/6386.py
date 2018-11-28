#include "cstdio"
#include "cmath"
#include "cstdlib"
#include "iostream"

using namespace std;

double p = 2.0;

int main(){
   freopen("B-large.in", "r",stdin);
   freopen("B-large.out","w",stdout);
   
   int t;
   cin >> t;
   
   for ( int caso = 1; caso <= t; caso++  ){
       double c, f, x;
       cin >> c >> f >> x;
       double n = 0.0;
       double sol = x/p; //solucion inicial
       double solTmp, sumatoria = 0.0;
       
       while ( true ){
             sumatoria = sumatoria + (c/(p+n*f));
             n = n + 1.0; //n : numero de fabricas
             solTmp = sumatoria + (x/(p+n*f));
             if ( solTmp < sol )
                sol = solTmp;
             else
                break;
       }//
       
       cout << "Case #" << caso << ": ";
       printf("%.7lf\n",sol);
       
   }//f caso  
           
   return 0;
}//fp
