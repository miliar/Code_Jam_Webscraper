#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
#define ANS 1023
int out = 0;
void add_digits(int num);
int main() {
	int t;
	int n,ans=0;
	cin >> t;
	 for(int i =0;i <t;i++){
	 	out = 0;
	 	cin >> n;
	 	ans =0;
	 	int count1=0;
	 	while( count1 < 100){
	 		ans +=n;
	 		add_digits(ans);
	 		count1++;
	 		if((out & ANS) == ANS){
	 			break;
	 		}
	 	}
	 	if((out & ANS) == ANS){
	 		cout << "Case #" << (i+1) << ": "<< (ans) << endl;
	 	}
	 	else{
	 		cout << "Case #" << (i+1) << ": "<<"INSOMNIA"<< endl;
	 	}
	 }	
	return 0;
}
void add_digits(int num){
	while(num){
		out = out | 1 << (num%10);
		num = num /10;
	}
}