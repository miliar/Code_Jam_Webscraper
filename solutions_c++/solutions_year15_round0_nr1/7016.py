#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;





int main(){
	
	int t;
	vector<int> v;
	long int sMax;
	string num;
	cin >> t;
	
	for(int i = 1; i <= t; ++i){
		cout << "Case #" << i << ": ";
		cin >> sMax;
		cin >> num;
		//cout << num << endl;
		long int acum = 0;
		long int max = 0;
		//vector<int> nums = toVector(num);
		for (int i = 0; i < num.size(); ++i){
			//cout << "acum+max: " << acum+max << endl;
			if (acum+max < i ){
				max += i - (acum+max);
			}
			acum+=num[i]-48;
			//cout << "i: " << i << endl;
			//cout << "num: " << (num[i]-48) << endl;
			//cout << "max: " << max << endl;
		}
		cout << max;
		
		cout << endl;
	}
	return 0;
}


