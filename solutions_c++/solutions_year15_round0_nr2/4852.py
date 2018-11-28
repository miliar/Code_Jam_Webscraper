#include <iostream>
#include <string>
#include <stdlib.h>
#include <vector>
#include <sstream>
#include <algorithm>
#include <map>
#include <stdbool.h>

using namespace std;

struct myclass {
  bool operator() (int i,int j) { return (i<j);}
} myobject;

struct combo {
	int num1;
	int num2;
};

std::map <int, struct combo > map1;

int splitornot(vector <int> vec, int min_vector, int *no1, int *no2, bool flag)
{
	int sum = 0;
	for(std::vector<int>::iterator iter = vec.begin(); iter != vec.end(); ++iter) {
	//	cout << *iter << "\t";
    		sum += *iter;
	}
	//cout << endl;

	//cout << "Sum obtained: " << sum << endl;
	
	if (sum <= 0)
		return 0;

	std::vector <vector <int> > newVec;
	std::vector <vector <int> >::iterator it;
	std::vector <int> ::iterator vec_iter;
	
	sort(vec.begin(), vec.end(), myobject);

	//cout << "Sort was okay" << endl;
	int max = vec.back();

	//cout << "Max obtained" << max << endl;
	std::vector <int> temp(vec);

	for (vec_iter = temp.begin(); vec_iter != temp.end(); vec_iter++) {
		if ((*vec_iter) > 0)
			(*vec_iter)--;
	}
	newVec.push_back(temp);
	//cout << "Reached here" << endl;

	vec.pop_back();
	if (max > 1) {
	/*
	map<int, struct combo >::iterator it_map = map1.find(max);
	*/
        if (flag & max > 3) {
		std::vector <int> newtemp(vec);
		newtemp.push_back(map1[max].num1);
		newtemp.push_back(map1[max].num2);
                newVec.push_back(newtemp);	
	} else	
	for (int i = 1; i <= max/2; i++) {
		std::vector <int> newtemp(vec);
		newtemp.push_back(i);
		newtemp.push_back(max - i);
		newVec.push_back(newtemp);
	}
		/*
		vec.push_back(max/2);
			if (max % 2 == 0)
				vec.push_back(max/2);
			else
				vec.push_back(max/2 + 1);
		cout << "Max /2 " << max/2 << endl;
		newVec.push_back(vec);*/
	}

	int min = min_vector;
	int num1;
	int num2;
       	for (it = newVec.begin(); it != newVec.end(); it++) {
		 int returned = 1 + splitornot(*it, min, no1, no2, flag);
		 if (min >= returned) {
			min = returned;
			num1 = ((*it).back());
			num2 = max - num1;
		}
	}
	//cout << "Min " << min << "  " << num1 << " " << num2 << endl;
	*no1 = num1;
	*no2 = num2;	
	return min;	
}




int main()
{
        int num;
        int d;
        int iter = 0;
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

	for (int i = 4; i <= 9; i++) {
		std::vector <int> initial;
		int no1;
		int no2;
		initial.push_back(i);
		splitornot(initial, i, &no1, &no2, false);
		map1[i].num1 = no1;
		map1[i].num2 = no2;
		//cout << map1[i].num1 << map1[i].num2 << endl;
	}
		
        while (iter < num) {

		cin >> d;
		int obtain_num;
		std::vector <int> vec;

		cin >> obtain_num;
		vec.push_back(obtain_num);

		getline(cin, get_case);
		//cout << "D is " << d << "Get case "<< get_case << endl;
		
		stringstream ss(get_case);
		int max = obtain_num;
		while (ss >> obtain_num) {
			vec.push_back(obtain_num);
			if (max < obtain_num)
				max = obtain_num;
		//	cout << obtain_num << endl;
		}
		//cout << "Max obtained" << max << endl;
		int num1;
		int num2;
		int ans = splitornot(vec, max, &num1, &num2, true);
		cout << "Case #" << iter + 1 << ": " << ans << endl;
		
		iter++;
        }
	return 0;
}
