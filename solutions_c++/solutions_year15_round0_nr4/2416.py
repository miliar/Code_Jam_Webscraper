#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <cctype>
#include <algorithm>

using namespace std;

string solve_problem(int X, int R, int C){
  if(R*C % X != 0){
		return "RICHARD";
	}
	if(X == 1){
		return "GABRIEL";
	}
	int max;
	int min;
	
	if( C > R){
		max = C;
		min = R;
	}
	else{
		max = R;
		min = C;
	}
	if(max == 4){
		if( min == 4){
				return "GABRIEL";
			}
		if( min == 3){
			return "GABRIEL";
		}
		if( min == 2){
			if(X == 4){
				return "RICHARD";
			}
			else{
				return "GABRIEL";
			}
		}
		if(min == 1){
			if( X == 3 || X == 4){
				return "RICHARD";
			}
			else{
				return "GABRIEL";
			}
		}
	}

	if(max == 3){
		if( min == 3){
			if(X == 1 || X == 3){
				return "GABRIEL";
			}
			else{
				return "RICHARD";
			}
		}
		if(min == 2){
			if(X != 4){
				return "GABRIEL";
			}
			else{
				return "RICHARD";
			}
		}
		if(X == 1){
			return "GABRIEL";
		}
		else{
			return "RICHARD";
		}
	}

	if(max == 2){
		if(X == 2 || X == 1){
			return "GABRIEL";			
		}
		else{
			return "RICHARD";
		}
	}
	
	if(max == 1){
		if (X == 1){
			return "RICHARD";
		}
		else{
			return "GABRIEL";
		}
	} 


}

int main(){
	int num_cases;
	
	cin >> num_cases;

	for(int n =0; n< num_cases; n++){
		int X;
		int R;
		int C;

		cin >> X;
		cin >> R;
		cin >> C;		
	
		cout << "Case #" << n+1 << ": " << solve_problem(X, R, C) << endl;
	}
}
