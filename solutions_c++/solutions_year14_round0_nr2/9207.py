#include<stdio.h>
#include<string.h>
#include<iostream>
#include<iostream>
#include<string>
#include<list>
#include<iterator>


using namespace std;
struct cookie{

  double c;
  double f;
  double x; 
}temp;

//typedef arr1 arr;
int main() {

  double i,j;
  std::list<cookie> c;
  int tests,test_count=1;
  // std::list<int> ans1, ans2;  
  scanf("%d",&tests);


  if(1<=tests<=100){
   test_count=1;
   while(test_count<=tests) {
     scanf("%lf",&temp.c);
     scanf("%lf",&temp.f);
     scanf("%lf",&temp.x);
    
     if((1<=temp.c<=10000) && (1<=temp.f<=100) && (1<=temp.x<=100000)){
       c.push_back(temp);
   

     }//cookie condition ends

     test_count++;
   }//while loop ends
 
      test_count=1;
      list<cookie>:: iterator ic=c.begin();
      //list<arr>:: iterator imat2=mat2.begin();
      //list<int>:: iterator ians1=ans1.begin();
      //list<int>:: iterator ians2=ans2.begin();
      double cookie_per_sec;
      double no_farm_time;
      double time_c_cookies;
      double farm_time;
      double time;
        
      while(test_count<=tests){
         cookie_per_sec=2;
         time=0.0;
         while(1) {
            //check the time with given rate
            //printf("ic.x:%lf",(*ic).x);
            no_farm_time=(*ic).x/cookie_per_sec;
            time_c_cookies=(((*ic).c)/cookie_per_sec);
            farm_time=time_c_cookies+(((*ic).x)/(cookie_per_sec+(*ic).f));
         
            //if farm_time is smaller
            if(farm_time<no_farm_time){
  
               cookie_per_sec+=(*ic).f;
               time+=time_c_cookies;
             }
             else {
               time+=no_farm_time;
               break;
             } 
         }
     
         printf("\nCase #%d: %.7lf",test_count,time);
         test_count++;
         ic++;
     }//while loop ends
  }//if test_no condition ends  

  else {

      cout<< "large no of tests";

  }
  return 0;
  
}
