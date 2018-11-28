#include <iostream>

using namespace std;

void standing_ovation(int s_max, int * s){
	int n = s[0];
	int friends=0;
	for(int i=1; i<s_max+1; i++){
		if(i > n && s[i] > 0){
			friends += i-n;
			n+=i-n;
		}
		n+=s[i];
	}
	cout << friends << endl;
}

int main(){
	int t;
	int * s_max;
	int ** s;
	
	cin >> t;
	
	s_max = new int [t];
	s = new int * [t];
	
	char in;
	for(int i=0; i<t; i++){
		cin >> s_max[i];
		s[i] = new int [s_max[i]+1];
		for(int j=0; j<s_max[i]+1; j++){
			cin >> in;
			s[i][j] = in - '0';
		}
	}
	
	for(int i=0; i<t; i++){
		cout << "Case #" << i+1 <<": ";
		standing_ovation(s_max[i], s[i]);
	}
	return 0;
}