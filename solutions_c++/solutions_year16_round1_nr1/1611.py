#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main(){
	ifstream cin("A-large (1).in");
	ofstream cout("out.out");
	int t, i, o = 0, first, last;
	char a[2010];
	string s;
	cin >> t;
	while (t--){
		o++;
		cin >> s;
		cout << "Case #" << o << ": ";
		for (i = 0; i < 2010; i++){
			a[i] = 0;
		}
		a[1001] = s[0];
		first = 1000;
		last = 1002;
		for (i = 1; i < s.length(); i++){
			if (s[i] >= a[first + 1]){
				a[first--] = s[i];
			}
			else{
				a[last++] = s[i];
			}
		}
		for (i = 0; i < 2010; i++){
			if (a[i] != 0){
				cout << a[i];
			}
		}
		cout << endl;
	}
	return 0;
}