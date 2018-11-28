#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


bool have_seen(int * n){
	bool flag = true;
	for(int i = 0; i < 10; i++){
		if(n[i] == 0){
			flag = false;
			break;
		}
	}
	return flag;
}


int main(){
	int T;
	long N;
	int first, last, n, i = 0, j =1;
	cin >> T;
	while(T){
		cin >> N;
		n = N;
		int idx[10] = {0};
		bool flag = false;
		int mul = 1;
		while(1){
			last = N;
			while(N){
				i = N % 10;
				idx[i]++;
				if(have_seen(idx)){
					flag = true;
					break;
				}
				N = N / 10;
			}
			if(flag){
				cout << "Case #" << j << ": " << first << endl;
				break;
			}
			mul++;
			first = n * mul;
			if(last == first){
				cout << "Case #" << j << ": INSOMNIA" << endl; 
				break;
			}
			N = first;
		}
		T--;
		j++;
	}
	return 0;
}
