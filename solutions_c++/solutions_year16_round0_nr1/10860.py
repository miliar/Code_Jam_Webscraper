#include <cstring>
#include <iostream>
#include <fstream>
using namespace std;

bool temp[10];

bool finish(){
	for (int i=0;i<=9;i++){
		if (temp[i]==false)return false;
	}
	return true;
}



int main () {
//	ifstream cin("A-large.in");
//	ofstream cout("A-large.out");
	int N,n,cnt=1;
	cin >> N;
	while (N--){
		cin >> n;
		memset(temp,false,sizeof(temp));
		int original = n;
		if (n==0){
			cout << "Case #" << cnt++ << ": INSOMNIA\n";
			continue;
		}
		string s;
		bool done = false;
		while (!done){
			s = to_string(n);
			for (int i=0;i<s.size();i++){
				temp[s[i]-'0'] = true;;
				if (finish()) {
					cout << "Case #" << cnt++ << ": " << n << endl;
					done = true;
					break;
				}
			}
			n+=original;
		}
	}
}
