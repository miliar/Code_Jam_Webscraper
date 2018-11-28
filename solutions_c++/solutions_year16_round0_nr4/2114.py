#include <iostream>

using namespace std;




int main (){
	FILE* ifile = freopen("D-small-attempt1.in", "r", stdin);
	FILE* ofile = freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for (int z=1; z<=t; z++){
		int k,c,s;
		cin >> k >> c >> s;
		long long start = 1;
		for (int i=1; i<=c-1; i++){
			start = start*k;
		}
		cout << "Case #" << z << ":";
		for (int i=1; i<=k; i++){
			cout << " " << i*start;
		}
		cout << endl;
	}
	
	
}
