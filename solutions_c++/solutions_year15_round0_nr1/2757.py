#include <iostream> 
#include <fstream> 
#include <math.h>

using namespace std;

int funA(int Smax, int S){
	int iter = pow(10, Smax);
	int clappers = 0;
	int invite = 0;
	
	for(int i = 0; i <= Smax; i++){
		if(clappers < i){
			invite += i - clappers;
			clappers = i;
		}
		clappers += S / iter;
		
		S %= iter;
		iter /= 10;
	}
	
	return invite;
}

int main() {	
	ifstream input("A-small-attempt0.in");
	ofstream output("output.ou");

	int sets, n;
	int Smax, S;
	
	if(input.is_open()){
		input >> sets;
		n = 1;
		
		while(sets > 0){
		
			input >> Smax >> S;
		
		
			//cout << Smax << " " << S << "\n";		
			output << "Case #" << n << ": " << funA(Smax, S) << "\n";
			
		
		
			sets--;
			n++;
		}
		
		input.close();
		output.close();
	}
	
	return 0; 
}
