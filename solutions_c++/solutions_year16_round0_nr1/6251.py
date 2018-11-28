#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int get_all_digits_seen(int n);
bool all(bool nums[]);

int main() {
	ifstream in("A-large.in");
	ofstream out;
	vector <int> nums;
	
	int num_cases;
	in >> num_cases;
	while ( num_cases > 0){
		int ncase;
		in >> ncase;
		nums.push_back(get_all_digits_seen(ncase));
		num_cases--;
	}
	out.open("A-large-out.txt");
	for(int i = 0; i < nums.size(); ++i){
		out << "Case #" << i+1 << ": ";
		if (nums[i] == 0)
			out << "INSOMNIA\n";
		else
			out << nums[i] << "\n";
	}
	
	return 0;
}

int get_all_digits_seen(int n){
	int i;
	if (n == 0)
		return 0;
	bool seen[] = {false, false, false, false, false, false, false, false, false, false};
	for (i = 1; (!all(seen)) && i < 1000000; ++i){
		int num = n * i;
		while (num > 0){
			seen[num % 10] = true;
			num /= 10;
		}
	}
	
	return (--i) * n;
	
}

bool all(bool nums[]){
	bool done = true;
	for (int i = 0; done && i < 10; i++)
		done = nums[i];
	return done;
}