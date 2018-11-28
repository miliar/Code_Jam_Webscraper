#include <iostream>
#include<cstdio>
#include<bits/stdc++.h>

using namespace std;
#define MAX 2009
#define min(a,b) (a>b?b:a)
#define max(a,b) (a>b?a:b)
//#define OJ
#ifndef OJ
	ifstream in("input.in");
	ofstream out("output.out");
	#define cin in
	#define cout out
#endif

int main(){
   int t,T;
   double c,f,x,par,fac,min,pnlty;
   cin>>T;
   for(t=1;t<=T;t++){
       //scanf("%f%f%f",&c,&f,&x);
       cin>>c>>f>>x;
       fac = 2.0;
       min = x/fac;
       pnlty = 0;
       while(true){
           par = c/fac + pnlty;
           pnlty = par;
           fac += double(f);
           par = par + (x/fac);
           if(par<min){
                min = par;
                //cout<<min<<'\n';
           }
            else
                break;
       }
       //printf("%.7lf\n",&par);
       //std::cout.precision(9);
       //cout<<min<<'\n';
       cout<<"Case #"<<t<<": ";
       cout<<fixed<<setprecision(7)<<min<<'\n';
   }
   
   return 0;
}

