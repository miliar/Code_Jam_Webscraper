#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <iomanip>
using namespace std;
#include <stdio.h>
#include <cstdio>

double bestTime(double C, double F, double X);
double timeNFarms(double C, double F, double X, int N);

int main(){
   int i,T;
   double results[1000];
   scanf("%d",&T);
   
   for(i=1; i<T+1;i++){
	   double C,F,X;
	   cin>>C>>F>>X;
	   results[i] = bestTime(C,F,X);
   }

   for(i=1; i<T+1;i++){
	   cout << "Case #"<<std::setprecision(20)<<i<<": " << results[i] << endl;

   }


   system("pause");
   return 0;
}


double bestTime(double C, double F, double X){
	double least = X/2; //default time when no farms bought
	int n=1;
	int i;
	while(timeNFarms(C,F,X,n)<=least){
		least = timeNFarms(C,F,X,n);
		n++;
	}
	/*for(i=0; i<20000; i++){
		if(timeNFarms(C,F,X,i)<=least) least = timeNFarms(C,F,X,i);
	}*/
	//cout<<i<<endl;
	return least;
}


double timeNFarms(double C, double F, double X, int N){
	double total=X/(2+N*F);
	int i;
	for(i=0; i<N; i++){
		total += C/(2+i*F);
	}

	return total;
}