#include <iostream>
#include <conio.h>
#include <fstream>
#include <time.h>

using namespace std;



int main(){

	int times;
long	double c,f,x,cookies=2 ,time2=0.0;
long	double time1=0.0, temp=0;
	int count, no=1;
	
	
	
	ifstream infile("B-large.in");
	ofstream outfile("output.txt");
	infile >> count;


	
	do{
	
	infile>> c >>f >>x;

	
	
		
	
	time1=x/cookies;	
		
	
	while(1){	
		
	
	

	
	
		temp=c/cookies;
		cookies+=f;
		
		time2+=temp+ (x/cookies);
		

				
		if(time2<time1){
			
			time1=time2;
			time2-= (x/cookies);
				
			
		continue;
	}
		else
		break;
		
		}
		outfile.precision(7);
		outfile.setf(ios::fixed);
		outfile.setf(ios::showpoint);
		outfile <<"Case #" << no  <<": " <<time1 <<endl;
		no++;
		count--;
	
	time1=time2=0;
	cookies=2;
	
		
	}while(count!=0);
		
	}
	
	
	
	
	
	
	
	

