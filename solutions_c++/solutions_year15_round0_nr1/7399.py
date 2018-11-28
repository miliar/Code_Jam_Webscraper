#include <iostream>
using namespace std;

int main(){
	string s;
	int times, maxShy;
	int minFriends;
	cin >> times;
	for (int i=0; i<times; i++){
		cin >> maxShy;
		cin >> s;
		minFriends = 0;
		int sum=0;
		for (int i=0; i<=maxShy; i++){
			if (sum < i){
				minFriends++;
				sum++;
			}
			sum += (s[i]-'0');
		}
		cout << "Case #" << i+1<< ": " << minFriends <<"\n";
	}
}
