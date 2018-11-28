#include<iostream>
#include<set>
#include<vector>
#include<string>
#include<string.h>

using namespace std;

void solve(char* s) {
	int n = strlen(s);
	int c = 0;
	while (n > 0 && s[n-1] == '+')
		n--;
	while (n) {
		if (s[0] == '+') {
			int i = 0;
			while (s[i] == '+') {
				s[i] = '-';
				i++;
			}
			c++;
		}
		else {
			for (int i =0; i < n; i++)
			  if (s[i] == '+')
			    s[i] = '-';
			  else
			    s[i] = '+';
			while (n > 0 && s[n-1] == '+')
		      n--;
		    c++;
			  
		}
	}
	cout << c;
}


int main() {
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    char s[105];
    cin >> s;
    solve(s);
    cout << endl;
  }
  return 0;
}

