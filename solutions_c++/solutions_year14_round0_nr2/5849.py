#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>  
#include <stdlib.h>  
#include <iomanip>
using namespace std;

int main(){
	ifstream in("E:\\Academic\\OJ\\pat\\google jam\\B-large.in"); 
	ofstream out("A-small-attempt0.out"); 

   if (! in.is_open())  
   { cout << "Error opening file"; exit (1); } 
	
	int N;
	in>>N;
	
	int casenum=1;
	while(N--){
		double answer=0; 
		double c,f,target;
		double x=0; //current cookie
		in>>c>>f>>target;
		double k=2; //current speed
		int i=1;
		double t0=0,t1=0, t;
		double xjiao=0;
		while(1){
			t=c/k;
			t1=t0+t;
			xjiao=k*(k+f)*t/f;
			if(target <= xjiao) break;
			t0=t1;
			k+=f;
		}
		answer=t0+target/k;
		out<<"case #"<<casenum++<<": ";
		out<<fixed<<setprecision(7)<<answer<<endl;
	}
	out.close();
	return 0;
}
