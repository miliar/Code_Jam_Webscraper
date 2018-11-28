#include <iostream>
#include <string>
//#include <set>
#include <fstream>
 
int main() {
 
	//std::set<int> digits;
	//int cases,n;
	//int final;
	//std::ifstream infile("A-large.in");
	//std::ofstream outfile("out.txt");

	//infile >> cases;
 //
	//for(int i=1; cases !=0; i++){
	//	infile >> n;
	//	for(int j=0; j<=9; j++){
	//		digits.insert(j);
	//	}
	//	if(n==0){
	//		outfile << "Case #" << i << ": " << "INSOMNIA" << std::endl;
	//	}
	//	else{
	//		for (int k=1; !digits.empty(); k++){
	//			final = n*k;
	//			std::string s = std::to_string(n*k);
	//			for(char& c : s) {
	//				digits.erase(c-'0');
	//			}
	//		}
	//		outfile << "Case #" << i << ": " << final << std::endl;
	//	}
	//	cases--;
	//}
	//outfile.close();

	int cases;
	std::string s;
	std::ifstream infile("B-large.in");
 	std::ofstream outfile("test1.out");
	infile >> cases;
	
	for(int i=1; cases !=0; i++){
		infile >> s;
		int moves = 0;
		if(s.find("-") == std::string::npos){
			outfile << "Case #" << i << ": " << moves << std::endl;
		}
		else {
			for(std::string::iterator it = s.begin(); it != s.end()-1; ++it)
			{
				if(*it != *(it+1)) {
					std::cout << *it << *(it+1) << std::endl;
					moves++;
				}
			}
			if(s.back() == '-'){
				moves++;
			}
			outfile << "Case #" << i << ": " << moves << std::endl;
		}
		cases--;
	}



	return 0;
}