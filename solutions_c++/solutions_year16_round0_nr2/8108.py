#include <iostream>
#include <string>

using namespace std;

int main(){
  int T = 0;
  cin >> T;

  for(int t = 0; t < T; ++t){
		string side;
		int ans = 0;

		cin >> side;
		//cout << side << endl;

		int s = side.size() - 1;
		for(; s >= 0; --s){
			if(side[s] == '-') break;
		}

		char cur = '+';
		for(; s >= 0; --s){
			if(cur != side[s]) ++ans;
			cur = side[s];
		}

		cout << "Case #" << (t+1) << ": " << ans << endl;
  }
}
