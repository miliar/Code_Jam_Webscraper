#include <iostream>
#include <string>
#include <set>
#include <fstream>
 
int main() {
 
	std::set<int> digits;
	int cases,n;
	int final;
	std::ifstream infile("A-large.in");
	std::ofstream outfile("out.txt");

	infile >> cases;
 
	for(int i=1; cases !=0; i++){
		infile >> n;
		for(int j=0; j<=9; j++){
			digits.insert(j);
		}
		if(n==0){
			outfile << "Case #" << i << ": " << "INSOMNIA" << std::endl;
		}
		else{
			for (int k=1; !digits.empty(); k++){
				final = n*k;
				std::string s = std::to_string(n*k);
				for(char& c : s) {
					digits.erase(c-'0');
				}
			}
			outfile << "Case #" << i << ": " << final << std::endl;
		}
		cases--;
	}
	outfile.close();
	return 0;
}