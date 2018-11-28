#include <iostream>
#include <map>
#include <list>
#include <string>

using namespace std;

int myints[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

void update_list(int num, list<int>& count){
	string s;	
	s = std::to_string(num);
	for(int i=0; i<s.size(); i++){
		int digit = s[i] - '0';
		count.remove(digit);
		//cout << digit << endl;
	}
}

void sleep(int num){
	list<int> count(myints, myints + sizeof(myints) / sizeof(int));
	int i = 1;
	int num1;
	while(1){
		num1 = num*i;
		//cout << "num: " << num1 << endl;
		if(num1 == 0){
			cout << "INSOMNIA";
			return;
		}
		update_list(num1, count);
		if(count.empty()){
			cout << num1;
			return;
		}
		i++;
	}
}

int main(int argc, char *argv[]) {
	int num_test;
	cin >> num_test;
	
	for(int i=0; i<num_test; i++){
		int num;
		cin >> num;
		cout << "CASE #" << i+1 << ": ";
		sleep(num);
		if(i != num-1)
			cout << endl;
	}
}