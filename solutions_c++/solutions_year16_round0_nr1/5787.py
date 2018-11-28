#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <queue>
using namespace std;



bool mark[10];
int cnt = 0;

void eval(int num){
    while(num){
	int left = num % 10;
	if(!mark[left]) { mark[left] = 1; cnt++; }
	num/=10;
    }
}

int main(){
    int T,N;
    cin >> T;
    for(int i=1;i<=T;i++){
	cin >> N;
	if(N == 0) {
	    cout << "Case #" << i << ": INSOMNIA" << endl;
	    continue;
	} 
	cnt = 0;
	for(int j=0;j<10;j++) mark[j] = 0;
	int cur = 0;
	while(cnt != 10){
	    cur += N;
	    eval(cur);
	}
	cout << "Case #" << i << ": " << cur << endl;
    }
    return 0;
}

