#include<iostream>
#include<cstdio>
#include<algorithm>
#include<set>
#include<vector>
#include<utility>
#include<map>
#include<list>
#include<queue>
#include<stack>
#include<cstring>
#include<string>
#include<cmath>
#include<cstdlib>
#include<fstream>
#include<cstdlib>
#include <iomanip>

using namespace std;



int main()
{


ifstream file;
ofstream out;
file.open("B-large.in");
out.open("large_output.txt");
int T;
file>>T;
 for(int t=1 ; t<=T ; t++){
    double C,F,X,rate(2),NumberOfCookies(0);
    double TotalTime(0.0000000000000);
   file>>C;
   file>>F;
   file>>X;
  
   // cout<<"C: "<<C<<" F: "<<F<<" X: "<<X<<endl;
    bool stop(0);
   while(!stop){
    
    double FarmeTime=(C/rate); 
    if( (TotalTime+(X/rate)) < (TotalTime+FarmeTime+(X/(rate+F) ) )){
      stop=true; 	
      TotalTime+=X/rate; 
	}
	else {
	  rate+=F;
	  TotalTime+=FarmeTime;  
     }
    
   
  }
    out << fixed << showpoint; 
    out << setprecision(7) ;
    out<<"Case #"<<t<<": "<<TotalTime<<endl;;
    //cout<<"rate: "<<rate<<" TotalTime: "<<TotalTime<<" condition: "<<stop<<endl; 
   
 
 }


    return 0;
}
