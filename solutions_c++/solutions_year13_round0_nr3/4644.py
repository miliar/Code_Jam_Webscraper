#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <cstring>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <fstream>

using namespace std;

bool palindrom(int num){

	string str;
	stringstream ss;
	ss << sqrt(num);
	ss >> str;

	int size = str.size();
	for(int i = 0 ;i < size/2 ;i++){
		if(str[i] != str[size-i-1])return false;
	}
	str = "";
	stringstream ll;
	ll << num;
	ll >> str;

	size = str.size();
	for(int i = 0 ;i < size/2 ;i++){
			if(str[i] != str[size-i-1])return false;
		}
	return true;
}




int main(){

#ifndef ONLINE_JUDGE
	 freopen("C-small-attempt0.in", "rt", stdin);
	  freopen("out.txt", "wt", stdout);
	 #endif


	 int tc = 0 ,t = 1 ,a = 0 ,b = 0,count = 0;

	cin >> tc;

	while(tc--){

		cin >> a >> b;

		for(int i = a;i <= b ;i++){
			if(palindrom(i))count++;
		}
		cout<<"Case #"<<t<<": "<<count<<endl;
		count = 0;
		t++;
	}


return 0;
}
//By : mohamed waleed
