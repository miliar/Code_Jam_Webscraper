#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

void probB();

int
main(void){
    int nTest;
    
    cin >> nTest;
    
    for(int i = 1; i <= nTest; i++){
        cout << "Case #" << i << ": ";
        probB();
    }
}

void probB(){
	double C, F, X;
	// C = Cost of Farm
	// F = Farm extra output
	// X = Win
	// Start Rate = 2 
	double rate = 2;

	cin >> C >> F >> X;

	double time = 0; 

    cout << setprecision(7) << fixed;

	// If X < C
	if(X < C){
		cout << X/2 << endl;
	}
	else{
		bool cont = true;
		while(cont){
			// Advance to decision point
			time += C/rate;
			
			double timeIfBuy = time + (X / (rate + F));
			double timeIfDontBuy = time + (X-C) / rate;
			if(timeIfBuy < timeIfDontBuy){
				rate += F;
			}else{
				time += (X - C) / rate;
				cont = false;
			}
		}

		cout << time << endl;
	}
	
}
