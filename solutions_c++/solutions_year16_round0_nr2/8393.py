#include<iostream>
#include<string>
using namespace std;
string s;
int size, sum;
void changer(int j){
	for(int i = 0; i <= j; i++){
		if(s[i] == '-') s[i] = '+';
		else s[i] = '-';
	}
	sum++;
}
int main(){
	int n;
	freopen("B-large.out", "w", stdout);
	cin >> n;
	for(int i = 0; i < n; i++){
		cin >> s;
		size = s.size();
		sum = 0;
		for(int  j = 0; j < size-1; j++){
			if(s[j] != s[j+1]) changer(j);
		}
		if(s[size-1] == '-') sum++;
		cout << "Case #" << i+1 << ": " << sum << endl;
	}
}
