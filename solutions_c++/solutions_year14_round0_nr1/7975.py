#include <iomanip>
#include <algorithm>
#include <iterator>     // std::insert_iterator
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <fstream>
using namespace std;

string num2str(int i) {stringstream ss; ss<<i; return ss.str();}

int main(){
	ifstream in("A.in");
	ofstream out("result.txt");
	int TESTS,M; 
	in >> TESTS;
	for(int test = 0; test<TESTS; test++){
		int r1,num;
		set<int> nums[2];
		vector<int> count(17,0);
		for(int k = 0; k<2; k++){
			in >> r1;
			for(int i = 0; i<4; i++)
				for(int j = 0; j<4; j++){
					in >> num;
					if(i == r1-1) nums[k].insert(num);
				}
		}
		
		set<int> inter;
		set_intersection(nums[0].begin(),nums[0].end(), 
						nums[1].begin(), nums[1].end(), 
						insert_iterator< set<int> >(inter, inter.begin()));

		string res  = "Case #";
		res += num2str(test+1); 
		res += ": ";
		if(inter.size() == 0)
			res += "Volunteer cheated!";
		else if(inter.size() == 1)
			res += num2str(*inter.begin());
		else
			res += "Bad magician!";


		cout << res << endl;
		out	 << res << endl;

	}
	return 0;
}
