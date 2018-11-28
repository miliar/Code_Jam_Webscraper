#include <iostream>
#include <string>
#include <sstream>
#include <set>
#include <vector>

using namespace std;

void phonenum(string num) {
	vector<int> count(26,0);
	vector<int> phone(10,0);
	for(int i = 0; i < num.size(); i++) {
		//cerr << num[i] << " " << num[i]-65 << " " << endl;
		count[num[i]-65]++;
	}
	// check Z
	if(count[25]!=0) {
		phone[0]+=count[25];
		count[4]-=count[25]; // E
		count[17]-=count[25]; // R
		count[14]-=count[25]; // O
		count[25]-=count[25]; // Z
	}
	// check W
	if(count[22]!=0) {
		phone[2]+=count[22];
		count[19]-=count[22]; // T
		count[14]-=count[22]; // O
		count[22]-=count[22]; // W
	}
	// check G
	if(count[6]!=0) {
		phone[8]+=count[6];
		count[4]-=count[6]; // E
		count[8]-=count[6]; // I
		count[7]-=count[6]; // H
		count[19]-=count[6]; // T
		count[6]-=count[6]; // G
	}
	// check U
	if(count[20]!=0) {
		phone[4]+=count[20];
		count[5]-=count[20]; // F
		count[14]-=count[20]; // O
		count[17]-=count[20]; // R
		count[20]-=count[20]; // U
	}
	// check X
	if(count[23]!=0) {
		phone[6]+=count[23];
		count[18]-=count[23]; // S
		count[8]-=count[23]; // I
		count[23]-=count[23]; // X
	}
	// check S
	if(count[18]!=0) {
		phone[7]+=count[18];
		count[4]-=count[18]; // E
		count[21]-=count[18]; // V
		count[4]-=count[18]; // E
		count[13]-=count[18]; // N
		count[18]-=count[18]; // S
	}
	// check V
	if(count[21]!=0) {
		phone[5]+=count[21];
		count[5]-=count[21]; // F
		count[8]-=count[21]; // I
		count[4]-=count[21]; // E
		count[21]-=count[21]; // V
	}
	// check O
	if(count[14]!=0) {
		phone[1]+=count[14];
		count[13]-=count[14]; // N
		count[4]-=count[14]; // E
		count[14]-=count[14]; // O
	}
	// check N
	if(count[13]!=0) {
		//cerr << "hello " << endl;
		int number = count[13]/2;
		phone[9]+=number;
		count[8]-=number; // I
		count[4]-=number; // E
		count[13]-=2*number; // N
	}
	// check T
	if(count[19]!=0) {
		//cerr << "Hi count 19 is " << count[19] << endl;
		phone[3]+=count[19];
		count[7]-=count[19]; // H
		count[17]-=count[19]; // R
		count[4]-=count[19]; // E
		count[4]-=count[19]; // E
		count[19]-=count[19]; // T
		//cerr << "count4 is " << count[4] << endl;
	}
	// check
	for(int i = 0; i < 26; i++) {
		//cout << i << " " << count.at(i) << " ";
		// if(count.at(i)!=0) {
		// 	cerr << "ERROR at " << i << endl;
		// }
	}
	for(int j = 0; j < 10; j++) {
		while(phone[j]) {
			cout << j;
			phone[j]--;
		}
	}
	cout << endl;
}

int main() {
	string line;
	int testNum;
	getline(cin, line);
	stringstream ss(line);
	ss >> testNum;
	int ct = 1;
	while(testNum > 0) {
		getline(cin, line);
		cout << "Case #" << ct << ": ";
		phonenum(line);
		testNum--;
		ct++;
	}
	return 0;
}