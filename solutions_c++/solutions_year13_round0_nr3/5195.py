#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<queue>
#include<map>
#include<set>
#include<string>
#include<vector>
#include<cstring>
#include<stack>
#include<climits>

using namespace std;

bool isPalindrome(int n){
	int flag = 1;
	int start,end;
	vector<int> vec;
	while(n != 0){
		vec.push_back(n%10);
		n/=10;
	}
	start = 0;
	end = vec.size()-1;
	while(start < end){
		if(vec[start] != vec[end]){
			flag = 0;
			break;
		}
		start++;
		end--;
	}
	return flag ? true : false;
}

bool isSquare(int n){
	int sq;
	sq = sqrt(n);
	return (sq*sq == n) ? true : false;
}

int main(){
	int T,test,ans,a,b;
	cin >> T;
	for(test=1;test<=T;test++){
		ans = 0;
		cin >> a >> b;
		for(int i=a;i<=b;i++){
			if(isPalindrome(i) && isSquare(i) && isPalindrome(sqrt(i))){
				ans ++;
			}
		}
		printf("Case #%d: %d\n",test,ans);
	}
	return 0;
}
