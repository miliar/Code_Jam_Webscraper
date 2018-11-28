#include <iostream>
#include <set>
using namespace std;


void helper(set<int>& s, int num, int & res){
	int cur_num = 0;
	if(num == 0){
		res = -1;
		return;
	}
	while(s.size() < 10){
		cur_num += num;
		while(cur_num > 0){
			s.insert(cur_num % 10);
			cur_num /= 10;
		}
		
	}
	res = cur_num;
	return;
}

int main(){
	int n;
	cin << n;
	set<int> s;
	for(int i = 0; i < n; i++){
		int cur, res;
		cin << cur;
		helper(s, cur, res);
		cout << "Case #" << i + 1 << <<": ";
		if(res == -1){
			cout << "INSOMNIA" << endl;
		} 
		else{
			cout << res << endl;
		}
	}	
}