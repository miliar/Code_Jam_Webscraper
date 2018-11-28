#include <iostream>

using namespace std;

void flip(char* s, int l, int r) ;

int main()
{
	int t;
	cin >> t;

	for(int q = 1; q <= t; ++q ) {
		char str[101];
		cin >> str;
		
		int initial, i = 0, count = 0;
		while(str[i] != '\0') {
			
			initial = i;

			if(str[i] == '+') {
				while(str[i] == '+') {
					i++;
				}
				if(str[i] == '\0')
					break;
				for(int a = initial; a < i; ++a) {
					str[a] = '-';
				}
			}	
			
			else {
				while(str[i] == '-') {
					i++;
				}
				for(int a = initial; a < i; ++a) {
					str[a] = '+';
				}
			}
				
			count++;
			
		}

		cout << "case #" << q << ": " << count << endl;
	}
}

void flip(char* s, int l, int r) 
{
	char temp = ' ';
	while(l <= r) {
		temp = (s[l] == '+' ? '-' : '+');
		s[l] = (s[r] == '+' ? '-' : '+');
		s[r] = temp;
		l++; r--;
	}

} 