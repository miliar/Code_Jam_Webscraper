#include<iostream>
#include<string.h>

using namespace std;
string flip(string, int);
char reverse(char);
int main() {
	
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, N, t, len, count;
	string s;
	cin >> T;
	t = 1;
	while(t <= T) {
		count = 0;
		cin >> s; 
		//cout << "Input: " << s << endl;
		len = s.size();
		for(int i = len-1; i >=0; i-- ) {
			
			int mul = 0, j = 0;
			while(s[j] == '+') {
				mul++;
				j++;
			} 
			if(mul > 0 && j < len) {
				s = flip(s, j-1);
				//cout << "Encountered + at begin: flipping at " << j-1 << " : " << s << endl;
				count++;
			}
		
			if(s[i] == '-') {
				s = flip(s, i);
				//cout << "After flipping at " << i << " : " << s << endl;
				count++;
			}
		}
		printf("Case #%d: %d\n", t, count);
		t++;	
	}
	
	return 0;
}
string flip(string s, int index) {
	char temp;
	
	for(int i = 0; i <= index/2; i++) {
		temp = reverse(s[i]);
		s[i] = reverse(s[index-i]);
		s[index-i] = temp;	
		//cout << "temp: " << temp << "9-i: " << (index-i)  << endl;
		//cout << "After swap :" << s << endl;
	}
	return s;
}

char reverse(char c) {
	if(c == '-')
		return '+';
	else 
		return '-';
}
