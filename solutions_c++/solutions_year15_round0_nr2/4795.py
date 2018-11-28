#include <bits/stdc++.h>
using namespace std;

int nomnom(vector<int> nums){
  int ans=999999, best, max=nums[nums.size()-1];
  
  for(int i=1; i<=max; i++){
  	best=0;
  	for(int j=0; j<nums.size(); j++){
  	  best+=ceil(1.0*nums[j]/i)-1;
  	}
  	ans=min(ans,best+i);
  }
  
  return ans;
}

int main() {
  int T, n, temp;
  cin >> T;
  
  for(int i=0; i<T; i++){
  	cin >> n;
  	vector<int> nums;
  	
  	for(int j=0; j<n; j++){
  	  cin >> temp;
  	  nums.push_back(temp);
  	}
  	
  	sort(nums.begin(), nums.end());
  	
  	cout << "Case #" << i+1 << ": " << nomnom(nums) << endl;
  }
}