//by Naciraa
#include <iostream>

using namespace std;

int main(){
	int t;
	cin >> t;
	int curr_case = 1;
	while(curr_case <= t){
		int k,c,s;
		cin >> k >> c >> s;
		cout << "Case #" << curr_case << ":";
		for(int i=1; i<s+1 ; i++){
			cout << " " << i;
		}
		cout << endl;
		curr_case++;
	}
	
	return 0;
}