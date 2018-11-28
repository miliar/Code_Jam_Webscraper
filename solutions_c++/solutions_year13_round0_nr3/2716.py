#include <iostream>
#include <sstream>
#include <cmath>
#include <limits>

using namespace std;

int executeloop();
bool ispal(int);
bool ispal(string);

int main(){
	int t;
	cin >> t;
	for(int i = 0; i < t; i++){
		cout << "Case #" << i+1 << ": " << executeloop() << endl;
	}
}

int executeloop(){
	int a, b, cnt = 0, low, high;
	cin >> a >> b;
	low = (int)(sqrt(a));
	high = (int)(sqrt(b)+1);
	for(int i = low; i <= high; i++){
		if(ispal(i) && ispal(i*i) && i*i >= a && i*i <= b){
			cnt++;
		}
	}
	return cnt;
}

bool ispal(int i){
	stringstream ss;
	ss << i;
	return ispal(ss.str());
}

bool ispal(string str){
	if(str.length() <= 1)
		return true;
	if(str[0] == str[str.length()-1])
		return ispal(str.substr(1,str.length()-2));
	return false;
}