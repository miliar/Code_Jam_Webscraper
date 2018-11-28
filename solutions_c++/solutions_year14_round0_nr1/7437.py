#include <algorithm>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

string answer(vector<int>);

int main(int argc, char **argv){
	size_t t;
	cin >> t;
	vector<int> v1, v2, v3;

	for(register size_t i = 0; i < t; i++){
		v1.clear(); v2.clear(); v3.clear();
		register int a;
		cin >> a;
		for(register int j = 1; j <= 4; j++){
			register int tmp;
			for(register int k = 0; k < 4; k++){
				cin >> tmp;
				if(j == a) v1.push_back(tmp);
			}
		}
		cin >> a;
		for(register int j = 1; j <= 4; j++){
			register int tmp;
			for(register int k = 0; k < 4; k++){
				cin >> tmp;
				if(j == a) v2.push_back(tmp);
			}
		}

		sort(v1.begin(), v1.end());
		sort(v2.begin(), v2.end());
		set_intersection(v1.begin(), v1.end(), v2.begin(), v2.end(), back_inserter(v3));
		cout << "Case #" << i + 1 << ": " << answer(v3) << endl;
	}

	return 0;
}

string answer(vector<int> v){
	stringstream ss;
	switch(v.size()){
		case 0:
			ss << "Volunteer cheated!";
			break;
		case 1:
			ss << v[0];
			break;
		default:
			ss << "Bad magician!";
			break;
	}
	return ss.str();
}
