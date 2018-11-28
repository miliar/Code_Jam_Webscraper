using namespace std;


#include <iostream> 
#include <algorithm> 
#include <iterator> 
#include <sstream> 
#include <fstream> 
#include <cassert> 
#include <climits> 
#include <cstdlib> 
#include <cstring> 
#include <string> 
#include <cstdio> 
#include <vector> 
#include <cmath> 
#include <queue> 
#include <stack> 
#include <deque> 
#include <stack> 
#include <list> 
#include <map> 
#include <set> 

#define D(x) //cout << #x " = " << (x) << endl

double costo, gan, total;
double rate = 2;
double acumGal, acumTime;
double getTotalTime(double tasa){
   return total / tasa;     
}
double getFarmTime(){
   return costo / rate;
}
void comprar(){
   acumTime += getFarmTime();
   acumGal -= costo;
   rate += gan;
}

int main(){
   // ios_base::sync_with_stdio(false);
    int n;
    cin >> n;
    int z = 1;
    while(n--){
       acumTime = acumGal = 0;
       rate = 2;
       cin >> costo >> gan >> total;
       while(getTotalTime(rate) > getFarmTime() + getTotalTime(rate + gan)){
          D(acumTime);
          comprar();                         
       }
       D(getTotalTime(rate) * rate);
       acumTime += getTotalTime(rate);
       
       cout << "Case #" << z << ": ";
       printf("%4.7f", acumTime);
       cout << endl;
       
       z++;
    }
    return 0;    
}
