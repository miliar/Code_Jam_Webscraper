#include <iostream>
#include <climits>
#include <vector>
using namespace std;


int solve(int n){
	int x = 1;
	int digits[10]={0};
	for (;x<INT_MAX;x++){
		int s = n * x;
		while(s > 0){
			digits[s%10] = 1;
			s/= 10;
		}
		if (digits[0] & digits[1] & digits[2] & digits[3] & digits[4] & digits[5] & digits[6] &digits[7] & digits[8] & digits[9] )
			return n * x;
	}
	return -1;
	
}
int main(int argc, char **argv)
{
	int test_cnt = 0;
	vector<int> nums;
        scanf("%d", &test_cnt);
	for (int i = 0; i < test_cnt; i++){
		int n;
		scanf("%d", &n);
		nums.push_back(n);
	}
        for (int i = 0; i < test_cnt; i++){
		int last = solve(nums[i]);
		if (last > 0)
			cout << "Case #"<<i+1<< ": "<< last << endl;
		else
			cout << "Case #"<<i+1<< ": INSOMNIA"<< endl;			
	}
	return 0;
}

