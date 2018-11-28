//by Naciraa
#include <iostream>
#include <vector>

using namespace std;

int countDigits(int n){
	vector< int> digits_seen(10,-1);
	int remaining = 10;
	int last_seen = n;
	int curr = n;
	int i = 1;
	while(remaining > 0){
		last_seen = curr;
		while(curr != 0){
			if(digits_seen[curr%10] == -1){
				digits_seen[curr%10] = 1;
				remaining--;
			}
			curr = curr/10;
		}
		i++;
		curr = i*n;
	}
	return last_seen;
}
int main(){
	int t;
	cin >> t;
	int curr_case = 1;
	while(curr_case<=t){
		int n;
		cin >> n;
		if (n == 0){
			cout << "Case #" << curr_case << ": INSOMNIA" << endl;
		}else{
			int res = countDigits(n);
			cout << "Case #" << curr_case << ": " << res << endl;
		}
		curr_case++;
	}
	return 0;
}
