#include <iostream>
#include <fstream>
using namespace std;
bool done(bool digits[]){
	for(int j=0;j<10;j++) if(!digits[j]) return false;
	return true;
}
int solve(int n){
    if(n == 0) return -1;

	int mult = 1;
	bool digits[10] = {};
	while(!done(digits)){
		int temp = n * mult;
		while(temp > 0){
			int ones = temp % 10;
			digits[ones] = true;
			temp /= 10;
		}
		mult++;
	}
	return n * (mult-1);
}
int main(){
    ifstream input("A-large.in");
    ofstream output("largeA.txt");
	int t;
	input >> t;
	for(int i=0;i<t;i++){
		int n;
		input >> n;
		cout << "Case #" << i+1 << ": ";
		output << "Case #" << i+1 << ": ";
		int ans = solve(n);
		if(ans == -1){
            cout << "INSOMNIA\n";
            output << "INSOMNIA\n";
		}
		else{
            cout << ans << endl;
            output << ans << endl;
		}
	}
	input.close();
	output.close();
	return 0;
}
