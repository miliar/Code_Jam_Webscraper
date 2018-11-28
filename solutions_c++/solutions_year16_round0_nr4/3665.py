#include<iostream>
#include<string>
#include<fstream>

using namespace std;

int main(){
	//ofstream out;
	//ifstream in;
	//in.open("D-small-attempt0.in");
	//out.open("sample.out");
	int t;
	cin >> t;
	int j = 1;
	while (t--){
		int k, c, s;
		cin >> k >> c >> s;
		cout << "Case #" << j << ": ";
		for (int i = 1; i <= s; i++) cout << i << " ";
		cout << "\n";
		//else cout << "Case #" << j << ": IMPOSSIBLE\n";
		j++;
	}
	//out.close();
	return 0;
}