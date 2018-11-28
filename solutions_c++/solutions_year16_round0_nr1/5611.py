#include <iostream>
#include <unordered_set>

using namespace std;

bool countingSheepUtil(int n, int &last_num) {

	if (n == 0) return false;

	unordered_set<int> s_nums;
	int i = 1;

	while (s_nums.size() < 10) {

		last_num = n * i;
		int curr_num = last_num;

		while (curr_num > 0) {
			s_nums.insert(curr_num % 10);
			curr_num = (curr_num - curr_num % 10)/10;
		}
		
		i++;

	}
	
	return true;

}


int main(int argc, char const *argv[])
{
	int n = 0;
	int last_num = 0;
	
	int test_case;
	
	cin >> test_case;
	
    for (int t = 1; t <= test_case; ++t) {
        cin >> n;
    	if (countingSheepUtil(n, last_num)) {
    		cout << "Case #" << t << ": " << last_num << endl;
    	} else {
    		cout << "Case #" << t << ": " << "INSOMNIA" << endl;
    	}
    }
    
	return 0;
}