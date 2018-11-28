#include <iostream>
#include <vector>
#include <ctime>
#include <fstream>
#include <iomanip>

char testcases[10], C[200], F[200], X[200];

long double t,c, f, x, noftime, timef, time2, rate, time1, nexttime;

bool test=true;

bool readInput(){
	std::ifstream inputFile;
    
    
        inputFile.open("problem2large.in");
 	
	if (!inputFile){
        	std::cout << "ERROR - File not found" << std::endl;
		return false;
    	}
	
	
	std::ofstream text;
	
	text.open("problem2large.out");
	
	if(!text.is_open()) return false;
	
   	inputFile >> testcases;
	
	t=atoi(testcases);
	
	//std::cout << "Analysing " << t << " cases"<< std::endl;
	
	for(int i=0; i<t; i++){
		
		inputFile >> C >> F >> X;
		
		c=atof(C);
		f=atof(F);
		x=atof(X);
		
		std::cout << std::setprecision(16) << c << " " << f << " " << x << std::endl;
		
		rate = 2;
		long double timet = 0;
		
		test=true;
		
		while (test){
			noftime = x/rate;
		
			timef = c/rate;
		
			rate=rate+f;
			
			nexttime = x/rate;
			
			time1 = noftime+timet;
			time2 = timef+timet+nexttime;

			if(time1<=time2){
				timet=time1;
				//std::cout << "timet " << timet << std::endl;
				test=false;
			}else{
				timet=timef+timet;
				//std::cout << "timet " << timet << std::endl;
				
			}
				
		}
		
		std::cout << "Case #" << i+1 << ": " << std::setprecision(16) << timet << std::endl;
		
		text << "Case #" << i+1 << ": " << std::setprecision(16) << timet;
		
		if(i!=t-1)
			text<<"\n";
		
	}
	
        inputFile.close();  
	text.close();

	
    	return true;
}

int main(void){

	readInput();
	
	return 1;
	
}
