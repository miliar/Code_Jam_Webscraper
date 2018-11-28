#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <climits>

using namespace std;

int get_minimum_time(std::vector<int> plates, int t){
	int total_pancake_count = std::accumulate(plates.begin(),plates.end(),0);
	if(total_pancake_count == 0)
		return t;
	std::vector<int> plates_copy = plates;
	// int old_size = plates.size();
	int result1 = INT_MAX, result2 = INT_MAX, result3 = INT_MAX;
	// cout << "plates.size1 - " << plates.size() << endl;
	for(int i=0; i<plates.size(); i++){
		plates[i] -= 1;
		if(plates[i] == 0){
			plates.erase(plates.begin()+i);
			i--;
		}
	}
	result1 = get_minimum_time(plates, t+1);
	// cout << "plates.size2 - " << plates.size() << endl;
	// cout << "result1 - " << result1 << endl;
	std::sort(plates_copy.begin(), plates_copy.end(), std::greater<int>());
	if(plates_copy[0] == 9){
		std::vector<int> plates_copy2 = plates_copy;
		plates_copy2[0] = 3;
		plates_copy2.push_back(3);
		plates_copy2.push_back(3);
		result3 = get_minimum_time(plates_copy2, t+2);
	}
	int half = plates_copy[0]/2;
	if(half > 0){
		plates_copy[0] -= half;
		plates_copy.push_back(half);
		result2 = get_minimum_time(plates_copy, t+1);
	}
	return min(min(result1, result2), result3);
	// cout << "result1 - " << result1 << " result2 - " << result2 << endl;
}

int main(){
	int test_cases, i=0, j=0, plate_count = 0, pancake_per_plate = 0, total_pancake_count = 0;
	cin >> test_cases;
	while(i++ < test_cases){
		j = 0;
		cin >> plate_count;
		std::vector<int> plates;
		while(j++ < plate_count){
			cin >> pancake_per_plate;
			plates.push_back(pancake_per_plate);
		}
		cout << "Case #" << i << ": " << get_minimum_time(plates, 0) << endl;
	}
	return 0;
}