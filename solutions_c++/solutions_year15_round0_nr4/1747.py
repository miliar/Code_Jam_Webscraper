#include <iostream> 
#include <fstream> 
#include <vector>

using namespace std;

int minspan(int n){
	if(n % 2 > 0)
		return n / 2 + n % 2;
	else
		return n / 2;
}

int main() {	
	ifstream input("D-large.in");
	ofstream output("output.ou");

	int sets, n;
	int X, R, C;
	bool done;
	
	if(input.is_open()){
		input >> sets;
		n = 1;
		
		while(sets > 0){
			
			input >> X >> R >> C;
			done = false;
			
			//donut case
			if(X > 6){
				output << "Case #" << n << ": RICHARD\n";
				done = true;
			}
			
			//obvious
			if(R * C % X > 0 && done == false){
				output << "Case #" << n << ": RICHARD\n";
				done = true;
			}
			
			//maxspan doesn't fit
			if(X > R && X > C && done == false){
				output << "Case #" << n << ": RICHARD\n";
				done = true;
			}
			
			//minspan doesn't fit
			if((minspan(X) > R || minspan(X) > C)  && done == false){
				output << "Case #" << n << ": RICHARD\n";
				done = true;
			}
			
			//minspan fits, uneven split
			if(minspan(X) == C && done == false){
				if(X == 4 || X == 6){
					output << "Case #" << n << ": RICHARD\n";
					done = true;
				}
				if(X == 5 && R <= 5){
					output << "Case #" << n << ": RICHARD\n";
					done = true;
				}
			}
			
			if(minspan(X) == R && done == false){
				if(X == 4 || X == 6){
					output << "Case #" << n << ": RICHARD\n";
					done = true;
				}
				if(X == 5 && C <= 5){
					output << "Case #" << n << ": RICHARD\n";
					done = true;
				}
			}
			
			
			//output << "Case #" << n << ": " << invite << "\n";
			if(done == false)
				output << "Case #" << n << ": GABRIEL\n";
			
		
		
			sets--;
			n++;
		}
		
		input.close();
		output.close();
	}
	
	return 0; 
}
