#include <cstdio>
#include <iostream>
using namespace std;


double X;    //Number of cookies to WIN
double F;    //RATE of cookies by farm
double C;    //FARM PRICE 

double total_time;
double nF;
double rate_ini = 2.0;
double rate;

double calculateTimeX(){
  rate = rate_ini + nF*F;

  return X/rate;
}

double calculateTimeC(){
  rate = rate_ini + nF*F;

  return C/rate;
}

int initialize(){
  nF = 0;
  total_time = calculateTimeX();
}

void process(){
  double tempo_acumulado = 0.0;
  double new_total_time = total_time - 0.0000001; //just to start

  while(new_total_time <= total_time){
    tempo_acumulado += calculateTimeC(); 
    nF++;
    new_total_time = tempo_acumulado + calculateTimeX();

    if(new_total_time < total_time) total_time = new_total_time;
  }
}


////////////////

int N;

void print_output(int case_n,double ans){
  printf("Case #%d: %.7lf\n",case_n,ans);
}

void read_input(){
  scanf("%lf %lf %lf", &C, &F, &X);
}


int main(){
  int case_n = 1;
  scanf("%d",&N);

   while(N--){
    read_input(); 

    initialize();
    process();

    print_output(case_n++,total_time);
   }



  return 0;
}

//double F;

//double time_lastSquare(int cookieInitial, double nF, int X){
//  return X / (cookieInitial + nF * F);
//}

//double time_lastSquare(int cookieInitial, double nF, int C){
//  return C / (cookieInitial + nF * F);
//}


