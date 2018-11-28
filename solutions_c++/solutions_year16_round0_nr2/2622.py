#include <iostream>


using namespace std;

char opp( char target){
	return target == '+' ? '-' : '+';
}

int countFlips ( std::string&  stack,  int flipUntil,  char target ){
	int flips = 0;
	if(flipUntil == 0){
		if( target ==  stack[flipUntil]) return 0;
		return 1;
	} 
	
	if( stack[flipUntil] == target){
		 flips = flips + countFlips( stack, flipUntil -1 , target);	
	}else{
		 flips = flips + countFlips( stack, flipUntil -1 , opp(target));
		 flips++;
	}
	return flips;
}

int main(){

	int T;
	cin>> T;
	for( int t=1; t <= T; t++){
		std::string stack;
		cin >> stack;
		cout << "Case #" << t <<": " << countFlips( stack, stack.size()-1,  '+')<<"\n";
	}
}