#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <vector>
#include <set>
#include <map>

using namespace std;

double solve(double C, double F, double X){
  double salary = 2.0;
 

  //case 1: if F>X, then don't need to buy Farm,
  if(C>=X)
    return X/salary;

   double cur = 0.0;
   double time = 0.0;
  //case 2: buy or not buy? This is a quesiton
  /*
    if remain time < get profit time 
         then not buy a new Farm: 
	 
	 remain time = (X-cur)/Salary
	 get profit time = C/F
   */
   while(1){
     //printf("%lf\n",time);
     if( cur<C ){
       double time_to_c = (C-cur)/salary;
       cur = C;
       time += time_to_c;
     }

     //buy or not
     if( (X-cur)/salary > (X-cur+C)/(salary+F) ){
       cur -= C;
       salary += F;
     }
     else
       break;
   }
   
   double remain_time = (X-cur)/salary;
   time += remain_time;
   return time;
}

int main(){
  int T;
  double C,F,X;
  int caseNum = 1;

  scanf("%d",&T);
  while(T--){
    //Cost C to buy a Fram which could product F per/second
    //the goal number of cookies is X;
    scanf("%lf%lf%lf",&C,&F,&X);
    printf("Case #%d: ",caseNum++);
    printf("%0.7lf\n",solve(C,F,X));
  }
  return 0;
}
