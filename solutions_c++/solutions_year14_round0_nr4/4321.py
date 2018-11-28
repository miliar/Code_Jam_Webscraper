#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
#include<iomanip>
#include<math.h>
#include<algorithm>

int main(int argc, char* argv[]){
	char* in_filename = "C:\\D-large.in", *out_filename = "C:\\out.out";
	std::ifstream in_file(in_filename);
	std::ofstream out_file(out_filename);
	std::string input = "", output = "", holder = "", answer = "";
	char test = ',';
	bool found_answer = false;
	long test_cases = 0, first_index = 0, second_index = 0, test_case_on = 0, counter = 0, turns = 0, index_chosen_1 = 0, index_chosen_2 = 0, int_answer_deceit = 0, int_answer_normal = 0, num_of_blocks = 0, index = 0;
	double *list1, *list2, *list1_copy, *list2_copy, chosen_n = 0, chosen_k = 0, told_n = 0;
	std::getline(in_file, input);
	test_cases = std::stoi(input);
	while (test_cases != test_case_on){
		
		turns = 0;
		int_answer_deceit = 0;
		int_answer_normal = 0;
		std::getline(in_file, input);
		num_of_blocks = std::stoi(input);
		list1 = new double[num_of_blocks];
		list2 = new double[num_of_blocks];
		list1_copy = new double[num_of_blocks];
		list2_copy = new double[num_of_blocks];
		std::getline(in_file, input);
		input += ' ';
		counter = 0;
		index = 0;

		while (counter != input.length()){
			holder = "";
			test = ',';
			while (test != ' '){
				test = input.at(counter);
				if (test == ' '){
					counter++;
					break;
				}
				holder += test;
				counter++;
			}
			list1[index] = atof(holder.c_str());
			list1_copy[index] = atof(holder.c_str());
			index++;
		}

		std::getline(in_file, input);
		input += ' ';
		counter = 0;
		index = 0;

		while (counter != input.length()){
			holder = "";
			test = ',';
			while (test != ' '){
				test = input.at(counter);
				if (test == ' '){
					counter++;
					break;
				}
				holder += test;
				counter++;
			}
			list2[index] = atof(holder.c_str());
			list2_copy[index] = atof(holder.c_str());
			index++;
		}
		
		counter = 0;
		first_index = 0;
		second_index = 0;
		index = num_of_blocks - 1;
		index_chosen_1 = num_of_blocks - 1;
		index_chosen_2 = num_of_blocks - 1;
		std::sort(list1, list1 + num_of_blocks);
		std::sort(list2, list2 + num_of_blocks);
		std::sort(list1_copy, list1_copy + num_of_blocks);
		std::sort(list2_copy, list2_copy + num_of_blocks);
	
		//deceit war//

		while (counter != num_of_blocks){
			found_answer = false;
			turns++;
			chosen_k = 1001;
			chosen_n = 1001;
			told_n = 1001;
			if (list2[second_index] == 0){
				second_index++;
			}
			if (list1[first_index] == 0){
				first_index++;
			}
			if (list1[first_index] < list2[second_index]){
				told_n = list2[index_chosen_2] - .005;
				chosen_k = list2[index_chosen_2];
				list2[index_chosen_2] = 0;
				chosen_n = list1[first_index];
				list1[first_index] = 0;
				first_index++;
				index_chosen_2--;
			}
			else if (list1[first_index] > list2[second_index]){
				told_n = list1[index_chosen_1];
				chosen_k = list2[second_index];
				list2[second_index] = 0;
				chosen_n = list1[first_index];
				list1[first_index] = 0;
				first_index++;
				second_index++;
				index_chosen_1--;
			}

			if (chosen_n > chosen_k){
				int_answer_deceit++;
			}
			
			counter++;
		}

		index_chosen_1 = 0;
		counter = 0;

		//normal war//

		while (counter != num_of_blocks){
			chosen_k = 1001;
			
			
			chosen_n = list1_copy[index_chosen_1];
			list1_copy[index_chosen_1] = 0;
			index_chosen_1++;
			for (int x = num_of_blocks - 1; x > -1; x--){
				if (list2_copy[x] > chosen_n && list2_copy[x] != 0){
					chosen_k = list2_copy[x];
					index_chosen_2 = x;
				}
			}
			list2_copy[index_chosen_2] = 0;
			if (chosen_n > chosen_k || chosen_k == 1001){
				int_answer_normal++;
			}
			counter++;
		}


		answer = std::to_string(int_answer_deceit) + ' ' + std::to_string(int_answer_normal);
		output += "Case #" + std::to_string(test_case_on + 1) + ": " + answer + '\n';
		test_case_on++;
	}
	in_file.close();
	out_file << output;
	out_file.close();
	
	return 0;
}