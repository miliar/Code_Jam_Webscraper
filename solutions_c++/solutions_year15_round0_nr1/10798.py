#include <iostream>
using namespace std;

int main() {
	int n,k;
	string ppl;
	cin >> n;
	for(int x=1;x<=n;x++){
		cin >> k >> ppl;
		int stand = 0,add = 0;
		for(int i=0;i<ppl.length();i++){
			if(stand < i){
				add += i-stand;
				stand += i-stand;
			}
			stand += ppl[i]-'0';
		}
		cout << "Case #" << x << ": " << add << endl;
	}
	return 0;
}