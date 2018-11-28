#include <iostream>
#include <cstdio>
#include<fstream>
using namespace std;

#define ll long long int

int main() {
	int t;
	ifstream fin;
	//ofstream fout;
	fin.open("B-large.in");
	//fout.open("output.txt");
	FILE *fp;
	fp = fopen("output.txt","w");
	//scanf("%d",&t);
	fin>>t;
	
	for(int k=1; k<=t; ++k) {
		double c,f,x;                 //cost of farm, production rate, required amount
        double rate=2.0,val=0.0;
		fin>>c>>f>>x;
		
		double time = 0.0;
		//val = 0;
		while(val < x) {
                  double timeLeft =(x)/rate;
                  double timeLeft2 = (c/rate) + x /(rate+f);
                  if(timeLeft <= 0 ) {
                              break;
                              }
                  
                  if( timeLeft < timeLeft2 ) {
                         //rate unchanged & val unchanged
                         time += timeLeft;
                         val =x;
                         }
                  else {
                        time += (c/rate);
                        rate += f;
                        val = 0;
                        }
                  
                  //cout<<"val= "<<val<<" rate= "<<rate<<endl;
                  }
                  
		//fout<<"Case #"<<k<<": "<<time<<"\n";
		fprintf(fp, "Case #%d: %0.7f\n",k,time);
	}
	
	fin.close();
	//fout.close();
	return 0;
}
