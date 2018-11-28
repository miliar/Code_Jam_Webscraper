#include <iostream>
#include <string>
using namespace std;

int revengeOfPanCakes(string str){
	int i,len = str.length();
	int count = 0;
	char last_sym = str[0];

	for(i=1; i<len; i++){
		if(str[i] != last_sym){
			last_sym = str[i];
			count++;
		}
	}
	if(last_sym == '-')
		return count+1;
	return count;
}
int main(){

	int N,i;
	string str;
	cin >> N;
	for(i=0; i<N; i++){
		cin >> str;
		cout <<"case #" << i+1 <<": " << revengeOfPanCakes(str) << endl;
	}
	return 0;
}
