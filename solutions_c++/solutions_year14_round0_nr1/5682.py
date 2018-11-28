#include<iostream>
#include<fstream>
#include<set>
#include<map>

int main(){
	//std::istream &input = std::cin;
	//std::ostream &output = std::cout;
	std::ifstream input_file("c:\\project\\A-small-attempt0.in");
	std::ofstream output_file("c:\\project\\A-small-attempt0.out");
	std::istream &input = input_file;
	std::ostream &output = output_file;

	int number_of_test_cases;
	input >> number_of_test_cases;
	for (int t = 1; t <= number_of_test_cases; t++){
		int first_answer;
		input >> first_answer;
		first_answer--;
		std::set<int> first_arrangement[4];
		int temp;
		for (int i = 0; i < 4; i++){
			for (int j = 1; j <= 4; j++){
				input >> temp;
				first_arrangement[i].emplace(temp);
			}
		}
		int second_answer;
		input >> second_answer;
		second_answer--;
		std::set<int> second_arrangement[4];
		for (int i = 0; i < 4; i++){
			for (int j = 1; j <= 4; j++){
				input >> temp;
				second_arrangement[i].emplace(temp);
			}
		}
		int count = 0, ele = -1;
		for (std::set<int>::iterator it = first_arrangement[first_answer].begin(); it != first_arrangement[first_answer].end(); it++){
			//ele = *it;
			if (second_arrangement[second_answer].find(*it) != second_arrangement[second_answer].end()){
				count++;
				ele = *it;
			}
		}
		if (count < 1){
			output << "Case #" << t << ": Volunteer cheated!" << std::endl;
		}
		else if (count == 1){
			output << "Case #" << t << ": " << ele << std::endl;
		}
		else{
			output << "Case #" << t << ": Bad magician!" << std::endl;
		}
	}
	input_file.close();
	output_file.close();
}