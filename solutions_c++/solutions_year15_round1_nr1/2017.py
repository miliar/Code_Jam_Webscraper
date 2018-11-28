//code compiled under g++ / c++11
#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>

using namespace std;
string solve_case(vector<int>&);

int main(void){
    int case_all;
	int N,temp;
	vector<int> mj;

    cin >> case_all;

    for(int i=1;i <= case_all;i++){
		cin >> N;

		for(int j=0;j<N;j++){
			cin >> temp;
			mj.push_back(temp);
		}
        cout << "Case #" << i << ": "
				<< solve_case(mj) << endl;
		mj.clear();
	}
}

string solve_case(vector<int>& mins){
	int ans_any =0;
	int ans_const =0;

	//any
	for(int i=1;i<mins.size();i++){
		if(mins[i-1] - mins[i] >0){//eaten
			ans_any += mins[i-1] - mins[i];
		}
	}

	//const
	int max_rate=0;
	for(int i=1;i<mins.size();i++){
		if(mins[i-1] - mins[i] >max_rate){
			max_rate = mins[i-1] - mins[i];
		}
	}

	for(int i=0;i<mins.size()-1;i++){
		if(mins[i] < max_rate){
			ans_const += mins[i];
		}else{
			ans_const += max_rate;
		}
	}

	return string(to_string(ans_any) + " " + to_string(ans_const));
}

