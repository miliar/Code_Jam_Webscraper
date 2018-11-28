#include <bits/stdc++.h>
using namespace std;


string replaceChar(string str, char ch1, char ch2) {
  for (int i = 0; i < str.length(); ++i) {
    if (str[i] == ch1)
      str[i] = ch2;
  }

  return str;
}

string flip(string s){
	s = replaceChar(s, '-', 'n');
	s = replaceChar(s, '+', 'p');
	s = replaceChar(s, 'n', '+');
	s = replaceChar(s, 'p', '-');
	return s;
}

void solve(){
	string stack;
	cin >> stack;

	if(stack.find("-") == string::npos){
		printf("%d\n", 0);
		return;
	}

	if(stack.find("+") == string::npos){
		printf("%d\n", 1);
		return;
	}

	int flips = -1;

	int ff;
	
	do{
		ff = stack.find_last_of("-");	
		if(ff == stack.length()){
			stack = flip(stack.substr(0,ff));
		} else {
			stack = flip(stack.substr(0,ff)) + stack.substr(ff+1,stack.length());
		}
		flips++;
	} while(ff != string::npos);

	printf("%d\n", flips);

	return;
}


int main ()
{
  	int cc;
  	cin >> cc;
	for (int dd = 1; dd <= cc; ++dd)
	{
  		printf("Case #%d: ", dd);
  		solve();
	}  
  	return 0;
}