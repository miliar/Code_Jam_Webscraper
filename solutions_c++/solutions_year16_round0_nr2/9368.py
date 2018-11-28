#include <iostream>
#include <vector>
using namespace std;



void pancake_sort(string str, int caseno){
	char flip = str[0];
	int flip_c = 0;
	if (str.size() == 1){
		if (flip == '-') cout <<"Case #"<< caseno << ": " << 1 << endl;
		if (flip == '+') cout <<"Case #"<< caseno << ": " << 0 << endl;
		return;
	}
	for (int i = 0; i < (str.size()-1); i++){
		if (str[i+1] != flip){
			flip_c++;
			flip = str[i+1];
		}
	}
	if (str[str.size()-1] == '-'){
		flip_c++;
	}
	cout <<"Case #"<<caseno<< ": " << flip_c << endl;
	return;
	
}
int main(int argc, char *argv[]) {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int tst;
	string str;
	cin >> tst;
	for (int i = 0; i < tst;i++){
		cin >> str;
		pancake_sort(str, (i+1));
	}
}