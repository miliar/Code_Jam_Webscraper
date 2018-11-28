#include <iostream>
#include <vector>
#include <math.h>
using namespace std;
int counter = 0;
long long twoToI(vector<int> &number, int length, int K){
	long long num = 0;
	
	for(int i = length-1; i >= 0; --i){
		num = num * K + number[i];
	}
	
	return num;
}

bool check(vector<int> &number, int length){
    vector<int> nontrivial(9,-1);
	for(int i = 2; i <= 10; ++i){
		long long num = twoToI(number, length, i);
		//cout << "k = " << i << " num = " << num << endl;
		bool ok = false;
		for(int j = 2; j <= (long long)floor(sqrt(num)+0.5); ++j){
			if(num % j == 0){
				ok = true;
				nontrivial[i-2] = j;
				break;
			}
		}
		if(ok == false){
			return false;
		}
	}
	
	for(int i = length-1; i >= 0; --i){
		cout << number[i];
	}	
	
	for(int i = 0; i < 9; ++i){
		cout << " " << nontrivial[i];
	}
	cout << endl;
	counter++;
}

void run(vector<int> &number, int length, int J, int cur){
	if(cur >= length - 1){
		check(number, length);
		return;
	}
	run(number, length, J, cur+1);
	if(counter >= J) return;
	number[cur] = 1;
	run(number, length, J, cur+1);
	if(counter >= J) return;
	number[cur] = 0;
}

int main(){
	//freopen("B2.in", "r", stdin);
	//freopen("myoutC2.out", "w", stdout);
	int T;
	cin >> T;
	
	for(int k = 1; k <= T; ++k){
	    int N,J;
	    cin >> N >> J;
	    cout << "Case #" << k << ": " <<endl;
	    
	    vector<int> number(N,0);
	    number[0] = 1;
	    number[N-1] = 1;
	    run(number, N, J, 1);
	}
	return 0;
}
