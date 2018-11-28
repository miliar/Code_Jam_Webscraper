#include <cmath>
#include <cstdio>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

string func(string s){
	int i, a[26];
	int len = s.length();
	
	int num[10];
	for(i=0;i<26;i++)
		a[i] =0;
	for(i=0;i<10;i++)
		num[i] = 0; 	
	for(i=0;i<len;i++){
		a[s[i]-'A'] +=1;
	}	
	num[0] = a[25]; //Z
	num[2] = a[22];	//W  	
	num[4] = a[20]; //U
	num[6] = a[23]; //X
	num[8] = a[6]; // G 

	a[18] -= num[6]; 
	a[14] = a[14] - num[0] - num[2] - num[4];
	a[17] = a[17] - num[0] - num[4];
	a[5] -= num[4];

	num[7] = a[18];
	num[1] = a[14];
	num[3] = a[17];
	num[5] = a[5];

	a[13] = a[13] - num[1] - num[7];
	num[9] = a[13]/2;

	string str;
	i=0;

	while(i < 10){
		if(num[i] > 0){
			while(num[i] > 0){
				str += to_string(i);
				num[i]--;
			}	
		}	
		i++;
	}
	return str;
}

int main() {

	/* Enter your code here. Read input from STDIN. Print output to STDOUT */

	int T;
	cin >> T;
	string s;
	for(int i=0;i<T;i++){
		cin >> s;
		cout << "Case " << "#"<<i+1 <<": "<< func(s)<<endl;
	}
	return 0;
}
