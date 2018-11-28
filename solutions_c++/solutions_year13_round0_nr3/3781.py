#include <iostream>
#include <math.h>
#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cctype>
#include <cstdio>
#include <cstdlib>

using namespace std;

int reverse(int num) {
	int rev = 0;
	while (num != 0) {
		rev = rev * 10 + num % 10;
		num /= 10;
	}
	return rev;
}

bool is_palindrome(int num){
	if(num == reverse(num)) return true;
	return false;
}

int main(){
/*
1 sqrt=> 1
4 sqrt=> 2
9 sqrt=> 3
121 sqrt=> 11
484 sqrt=> 22
*/

	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	vector<int> fair_nums;
	fair_nums.push_back(1);
	fair_nums.push_back(4);
	fair_nums.push_back(9);
	fair_nums.push_back(121);
	fair_nums.push_back(484);

	int caseno;
	scanf("%d",&caseno);
	for(int case_id=0;case_id<caseno;case_id++){
		int count_num=0,A,B;
		cin >> A >> B;
		for(int i=0;i<fair_nums.size();i++){
			if(fair_nums[i] >= A && fair_nums[i] <= B)
				count_num++;
		}
		cout << "Case #" << case_id+1 << ": " << count_num << endl;
	}

	/*
	for(int i=1;i<=1000;i++){
		if(is_palindrome(i)){
			int sqrt_num = sqrt(i);
			if(is_palindrome(sqrt_num) && (sqrt_num * sqrt_num == i))
				cout << i << " sqrt=> " << sqrt_num << endl;
		}
	}
	*/
	return 0;
}