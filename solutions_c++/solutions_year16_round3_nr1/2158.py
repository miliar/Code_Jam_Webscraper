#include <iostream>
#include <sstream>
#include <vector>
#include <unordered_map>
#include <string>

using namespace std;


int main(){
	//cout << int('A');//65
	int TC;
	cin >> TC;
	//cin.ignore();
	for(int tc=1;tc<=TC;tc++){
		cout << "Case #" << tc <<": ";
		int nums[26];
		memset(nums, 0, sizeof(nums));
		int n;
		cin >> n;
		for(int i=0;i<n;i++){
			cin >> nums[i];
		}
		int max = *std::max_element(nums,nums+n);
		int mycount = std::count (nums, nums+n, max);
		while(max!=0){
			if(max!=1 && mycount==1){
			 	int first = distance(nums, max_element(nums, nums + n));
			 	nums[first]--;
			 	cout << char(65+first);
			}else if(max!=1&& mycount==2){
			 	int first = distance(nums, max_element(nums, nums + n));
			 	nums[first]--;
			 	cout << char(65+first);
			 	int second = distance(nums, max_element(nums, nums + n));
			 	nums[second]--;
			 	cout << char(65+second);
			}else if(max==1 && mycount>2){
				int first = distance(nums, max_element(nums, nums + n));
			 	nums[first]--;
			 	cout << char(65+first);
			}else{
				int first = distance(nums, max_element(nums, nums + n));
			 	nums[first]--;
			 	cout << char(65+first);
			 	int second = distance(nums, max_element(nums, nums + n));
			 	nums[second]--;
			 	cout << char(65+second);
			}
			max = *std::max_element(nums,nums+n);
			mycount = std::count (nums, nums+n, max);
			if(max!=0)
				cout <<" ";
		}
		cout << endl;		
	}
}