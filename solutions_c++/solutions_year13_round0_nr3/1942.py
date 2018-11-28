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
#include <vector>

using namespace std;

typedef unsigned long long ll;

ll reverse(ll num) {
	ll rev = 0;
	while (num != 0) {
		rev = rev * 10 + num % 10;
		num /= 10;
	}
	return rev;
}

bool is_palindrome(ll num){
	if(num == reverse(num)) return true;
	return false;
}

vector<ll> isfair_square_num(ll A,ll B){
	vector<ll> nums;
	ll sqrt_a = sqrt(A);
	ll sqrt_b = sqrt(B);

	for(ll i=sqrt_a;i<=sqrt_b;i++){
		if(is_palindrome(i)){
			ll sqr_num = i * i;
			if(is_palindrome(sqr_num)&&(sqr_num >= A)&& (sqr_num <= B)){
				//count_num++;
				nums.push_back(sqr_num);
				//cout << sqr_num << "     sqrt=> " << i << endl;
			}
		}
	}

	return nums;
}

int main(){
	//vector<ll> nums = isfair_square_num(1,1000);freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
	vector<ll> nums = isfair_square_num(1,100000000000000);freopen("C-large-1.in","r",stdin);freopen("C-large-1.out","w",stdout);

	int caseno;
	scanf("%d",&caseno);
	for(int case_id=0;case_id<caseno;case_id++){
		ll count_num=0,A,B;
		cin >> A >> B;
		for(int i=0;i<nums.size();i++){
			if(nums[i] >= A && nums[i] <= B)
				count_num++;
		}
		cout << "Case #" << case_id+1 << ": " << count_num << endl;
	}
	return 0;
}