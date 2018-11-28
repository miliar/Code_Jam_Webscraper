#include <iostream>
#include <set>
using namespace std;

int main(){
	int n;
	cin >> n;
	for(int i = 0; i < n; i++){
		char cur;
		char next;
		next = getchar();
		cur = next;
		int total = 0;
		while(true){
			next = getchar();
			if(next == '\n'){
				break;
			}
			else{
				if(next != cur){
					total++;
					if(cur == '-'){
						cur = '+';

					}
					else{
						cur = '-';
					}
				}
			}
		}
		if(cur == '-'){
			total++;
		}
		cout << "Case #" << i + 1 << <<": " << total << endl;
	}
}