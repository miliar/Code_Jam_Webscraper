#include <iostream>
#include <string>

using namespace std;

void solve(int zap){
	int n;
	cin >> n;
	string s;
	cin >> s;
	int rez = 0;
	int plosk = 0;
	for(int i=0;i<n+1;i++){
		int tr = s[i]-'0';
		if(i>plosk){
			rez+=i-plosk;
			plosk = i;
		}
		plosk+=tr;
	}
	cout << "Case #" << zap << ": " << rez << "\n";
}

int main(){
	int st;
	cin >> st;
	for(int i=1;i<=st;i++)solve(i);
	return 0;
}
