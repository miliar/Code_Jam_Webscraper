#include<iostream>
#include<vector>

#define MN (1000 * 1000 * 10 + 1)

using namespace std;

bool isPalindrome(long long num);

int main(){
	long long arr[] = {0, 1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004,
	100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001,
	10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001,
	1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321,
	1234567654321, 4000008000004, 4004009004004};
	
	/*int number = 0;
	for(long long i = 0; i < MN; i++){
		if(isPalindrome(i) && isPalindrome(i*i)){
			v.push_back(i*i);
			number++;
		}
	}
	cout<< number << endl;*/
	
	long long testnum, a, b, ans;
	cin >> testnum;
	for(long long q = 0; q < testnum; q++){
		cout << "Case #" << q + 1 << ": ";
		cin >> a >> b;
		ans = 0;
		for(long long i = 0; i < 40; i++){
			if(arr[i] >= a && arr[i] <= b){
				ans++;
			}
		}
		cout << ans << endl;
	}
	return 0;
 
}

bool isPalindrome(long long num){
	vector<int> vtemp;
	vtemp.clear();
	while(num > 0){
		vtemp.push_back(num % 10);
		num /= 10;
	}
	for(int r = 0; r < vtemp.size()/2; r++){
		if(vtemp[r] != vtemp[vtemp.size() - r - 1]){
			return false;
		}
	}
	return true;
}
