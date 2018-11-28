#include<iostream>
#include<fstream>
#include<vector>

#define MAX 6

using namespace std;

int calc(vector<int>& nums, int s_max);

int main(int argc, char const *argv[])
{
	streambuf *iBackup = NULL , *oBackup = NULL;
	ofstream output;
	ifstream input;

	// backsup input/output
	iBackup = cin.rdbuf();
	oBackup = cout.rdbuf();
	
	input.open("input.in");
	
	if( input.fail()){
		cout << "input failed." << endl;
		return 1;
	}
	cin.rdbuf(input.rdbuf());
	
	output.open("output.out");
	if( output.fail()){
		cout << "output failed." << endl;
		return 1;
	}
	cout.rdbuf(output.rdbuf());
	
	int T=0;
	int s_max;
	char tmp;
	vector<int> nums;

	cin >> T;
	
	for(int i=1;i<=T;i++)
	{
		// input

		cin >> s_max;

		for(int j=0;j<=s_max;j++){
			cin >> tmp;
			int x = tmp - '0';
			nums.push_back(x);
			//cout << x << endl;
		}

		// input

		

		// output
		cout << "Case #" << i << ": " << calc(nums, s_max) << endl;

		nums.clear();
	}
	
	input.close();
	cin.rdbuf(iBackup);
	output.close();
	cout.rdbuf(oBackup);

	return 0;
}

int calc(vector<int>& nums, int s_max){
	int fromAudience = nums[0];
	int toAdd = 0;

	for(int i=1;i<nums.size();i++){
		if(fromAudience + toAdd < i){
			toAdd += i - (fromAudience + toAdd);
		}
		fromAudience += nums[i];
	}

	return toAdd;

}