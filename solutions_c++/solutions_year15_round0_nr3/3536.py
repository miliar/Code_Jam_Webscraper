#include <iostream>
#include <vector>

using namespace std;

int cvt(char c){
	return c - 'g';
}
char cvt(int n){
	return n + 'g';
}

int t[5][5] = {
	{ 0, 0, 0, 0, 0 },
	{ 0, 1, 2, 3, 4 },
	{ 0, 2,-1, 4,-3 },
	{ 0, 3,-4,-1, 2 },
	{ 0, 4, 3,-2,-1 }
};

void f(string& str, const int& i, const int& j, bool& isP){
	int c1 = cvt(str[i]);
	int c2 = cvt(str[j]);
	int c = t[c1][c2];
	if(c < 0){
		isP ^= true;
		c *= -1;
	}

	str = str.substr(0, i) + cvt(c) + str.substr(j+1, (str.size()-1 - j));
}

void debug(string str){
	cout<< str<< " "<< str.size()<< endl;
}

bool solve(){
	int dm, k;
	cin>> dm>> k;
	string s;
	cin>> s;
	string str;
	for(int i=0;i<k;i++) str += s;
	//cout<< endl; cout<< str<< endl;

	bool isP = true;
	// i(left)
	while(str.size() >= 3){
		if(str[0] == 'i') break;
		f(str, 0, 1, isP);
	}

	// k(right)
	while(str.size() >= 3){
		if(str[str.size()-1] == 'k') break;
		f(str, str.size()-2, str.size()-1, isP);
	}

	// j(middle)
	if(str.size() >= 3){
		string s = str.substr(1, str.size()-2);
		while(s.size() > 1){
			f(s, 0, 1, isP);
		}
		str = str[0] + s + str[str.size()-1];
	}

	//cout<< (isP ? "" : "-")<< str<< endl;
	if(isP && str == "ijk") cout<< "YES"<< endl;
	else cout<< "NO"<< endl;

	return true;
}

int main(){
	cout.setf(ios::fixed); cout.precision(10);
	int n;
	cin>> n;
	for(int i=0;i<n;i++){
		cout<< "Case #"<< i+1<< ": ";
		solve();
	}
	return 0;
}
