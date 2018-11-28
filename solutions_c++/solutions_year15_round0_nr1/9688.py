#include <iostream>
#include <string>
#include <stdlib.h>
#include <vector>

using namespace std;

int main()
{
        int num;
        int smax;
        int iter = 0;
        int do_while_iter = 0;
        std::string num_of_Testcases;
  	std::string get_case;
        
	/*std::getline(std::cin, num_of_Testcases);
        num = atoi(num_of_Testcases.c_str());
        if (num < 0)	
		return -1;
        */
	cin >> num;
	if (num < 0)
		return -1;
        while (iter < num) {
		cin >> smax >> get_case;
		//cout << smax << get_case << endl;
		std::vector <int > vec;
		std::string::iterator it;
		for (it = get_case.begin(); it != get_case.end(); it++) {
			vec.push_back(*it - '0');
		}
		int num_of_friends = 0;
		for (int vec_loop = 1; vec_loop <= smax; vec_loop++) {
			if (vec_loop > vec[vec_loop - 1] && vec[vec_loop] > 0) {
				//cout << "friends: " << num_of_friends << "loop: " << vec_loop << endl; 
				num_of_friends += vec_loop - vec[vec_loop - 1];
				vec[vec_loop] += num_of_friends + vec[vec_loop - 1];
			} else {
				vec[vec_loop] += vec[vec_loop - 1];
			}
		}
                cout << "Case #" << iter + 1 << ":" << " " << num_of_friends << endl;	
		iter++;
        }
	return 0;
}
