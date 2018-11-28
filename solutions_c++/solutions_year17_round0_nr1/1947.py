#include <iostream>
#include <vector>

void flip_start_index_to_N(std::vector<bool>& vec, int index, int num);
void print_vec(std::vector<bool>& vec);

int get_case(void) {
	int cases;

	std::cin >> cases;

	return cases;
}

int get_data(std::vector<bool>& vec) {
	int num;
	std::string pancakes;
	std::cin >> pancakes;

	for(char& c : pancakes) {
		if(c == '-') 
			vec.push_back(0);

		else if(c == '+') 
			vec.push_back(1);
	}

	std::cin >> num;
	return num;
}

int flip_complete(std::vector<bool>& vec, int k) {
	bool base = false;
	int count = 0;
	std::vector<bool>::iterator iter;

	for(iter = vec.begin() ; iter != vec.end() ;) {
		if(*iter == 0) {
			if(distance(iter, vec.end()) < k) {
				return -1;
			}
	
			flip_start_index_to_N(vec, iter-vec.begin(), k);
			count++;	
			iter++;
			continue;
		}
		
		if(iter < vec.end()) 
			iter++;
	}

	return count;
}


void flip_start_index_to_N(std::vector<bool>& vec, int index, int num) {
	std::vector<bool>::iterator iter;
	iter = vec.begin();

	advance(iter, index);

	for(int i = 0 ; i < num ; i++) {

		*iter = ~(*iter);
		if(iter == vec.end())
			break;

		else
			iter++;
	}
}


void print_vec(std::vector<bool>& vec) {
	std::vector<bool>::iterator iter;

	for(iter = vec.begin() ; iter != vec.end() ; iter++) 
		std::cout << *iter;

	std::cout << " ";
}


int main(void) {
	int cases = 0;
	int flipper = -1;
	int number = 1;

	std::vector<std::string> count;
	std::vector<bool> cakes;
	std::vector<std::string>::iterator iter;
	int res;

	cases = get_case();
	
	for(int i = 0 ; i < cases ; i++) {
		flipper = get_data(cakes);
		res = flip_complete(cakes, flipper);

		if(res == -1)
			count.push_back("IMPOSSIBLE");
		else
			count.push_back(std::to_string(res)); 

		cakes.clear();
	}


	for(iter = count.begin() ; iter != count.end() ; iter++) { 
		std::cout << "Case #" << number << ": " << *iter << std::endl;
		number++;
	}

}


