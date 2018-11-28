#include <iostream>
#include <string>
#include <deque>

using namespace std;

int main(int argc, char *argv[]){
	int repeat, repti, len, i;
	string s;
	deque<char> mydeck;
	
	cin >> repeat;
	for(repti = 0; repti < repeat; repti++){
		mydeck.clear(), s.clear();
		cin >> s;
		len = s.size();
		if(len == 0) break;
		mydeck.push_back(s[0]);
		for(i = 1; i < len; i++){
			if(s[i] >= mydeck[0]) mydeck.push_front(s[i]);
			else mydeck.push_back(s[i]);
		}
		len = mydeck.size();
		
		cout << "Case #" << repti+1 << ": ";
		for(i = 0; i < len; i++)
			cout << mydeck[i];
		cout << endl;
	}

	return 0;
}
