#include <iostream>  
#include <vector>
using namespace std;

string countsleep(int givennum) {
	if (givennum == 0) 
		return "INSOMNIA";
	vector<bool> check(10, 0);
	int n = givennum;
	int mul = 2;
	int cnt = 10;
	
	while (1) {
		string s = to_string(n);
		for(int i = 0; i < s.size(); i++) {
			if (check[s[i] - '0'] == 0) {
				cnt--;
				check[s[i] - '0'] = 1;
			}
		}
		if (cnt == 0) {
			break;
		}
		n = mul * givennum;
		mul++;
	}
	return to_string(n);
}

int main() {
  int numCase;
  cin >> numCase;
  int n;
  for (int i = 1; i <= numCase; ++i) {
	    cin >> n;  // read n.
		cout << "Case #" << i << ": " << countsleep(n) <<endl;

  }
 return 0;
}