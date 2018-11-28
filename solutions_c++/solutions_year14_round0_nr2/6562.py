#include <iostream>
#include <fstream>
#include <string>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include <iomanip>  
using namespace std;

int main () {
  string line;
  int T; double C,F,X; int k1;double sum;
  string Cs,Fs,Xs;
  ifstream myfile ("A-small-attempt0.in");
  std::ofstream out("out.txt");
  std::streambuf *coutbuf = std::cout.rdbuf();
  std::cout.rdbuf(out.rdbuf());
  if (myfile.is_open())
  {
    myfile >> T;
    for(int k=0;k<T;k++)
    {

            myfile >> Cs;
            myfile >> Fs;
            myfile >> Xs;
            //cout<<Cs<<endl;cout<<Fs<<endl;cout<<Xs<<endl;
            C=atof(Cs.c_str());X=atof(Xs.c_str());F=atof(Fs.c_str());
            //cout<<"C: "<<C<<endl;cout<<"F: "<<F<<endl;cout<<"X: "<<X<<endl;
            k1=0 ;sum=0;
            if(X>C)
            { 
		    while(((X/((k1+1)*F+2))+(C/(k1*F+2)))<(X/(k1*F+2))){
		      // cout<<((X/((k1+1)*F+2))+(C/(k1*F+2)))<<"__";cout<<(X/(k1*F+2))<<endl;
		       k1=k1+1;
		     }
		    for (int i = 0; i < k1; i++) 
		    sum=sum+(C/(i*F+2));
		    sum=sum+(X/(k1*F+2)); 
            }
            else sum=X/2;
            cout<<"Case #"<<k+1<<": "<< std::setprecision(12)<<sum<< endl;
     }
     myfile.close();
  }

  else cout << "Unable to open file"; 

  return 0;
}
