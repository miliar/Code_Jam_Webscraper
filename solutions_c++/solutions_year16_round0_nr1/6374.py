#include <iostream>
#include <fstream>
#include <set>

using namespace std;

int main(){

	ios::sync_with_stdio(0);

	set<int> s;
	ifstream input("A-large.in");
	ofstream output("output.txt");
	int t, num, count = 1, temp, c, num1;
	input >> t;

	while(t--){

		input >> num;
		if(!num){
			output << "Case #" << count++ << ": " << "INSOMNIA\n";
			continue;
		}

		c = 1;
		s.clear();
		while(s.size() != 10){
			temp = num * c++;
			num1 = temp;
			while(temp){
				s.insert(temp % 10);
				temp /= 10;
			}	
		}
		
		output << "Case #" << count++ << ": " << num1 << "\n";
	}
	

	return 0;
}