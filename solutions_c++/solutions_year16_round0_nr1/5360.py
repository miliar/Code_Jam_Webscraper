#include<iostream>
#include<string>
#include<fstream>

using namespace std;

int main(){
	//ofstream out;
	//ifstream in;
	//in.open("A-large.in");
	//out.open("sample.out");
	int t;
	cin >> t;
	int j = 1;
	int ans;
	int N, m;
	string s;
	int ch[10];
	bool ok;
	while (t--){
		cin >> N;
		ok = false;
		if (N == 1000000){
			ans = 9000000;
			ok = true;
		}
		else if (N == 0){
			ok = false;
		}
		else{
			m = N;
			for (int i = 0; i < 10; i++)ch[i] = 0;
			for (int i = 0; i <= 1000000; i++){
				s = to_string(m);
				for (int j = 0; j < s.length(); j++){
					ch[(s[j] - '0')]++;
				}

				ok = true;
				for (int j = 0; j < 10; j++){
					if (ch[j] == 0){
						m += N;
						ok = false;
						break;
					}
				}

				if (ok) {
					ans = m;
					break;
				}
			}
		}
		if (ok) cout << "Case #"<< j << ": "<< ans << "\n";
		else cout << "Case #" << j << ": INSOMNIA\n";
		j++;
	}
	//out.close();
	return 0;
}