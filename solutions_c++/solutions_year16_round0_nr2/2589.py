#include<string>
#include<sstream>
#include<iostream>
#include<algorithm>

using namespace std;


int main(){

	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	char c,sum = '-'+'+';
	string s;
	int res;

	int ntc;
	cin >> ntc;
	for (int tc=1;tc<=ntc;tc++){
		cin >> s;
		reverse(&s[0],&s[0]+s.length());
		res = 0;
		c = '-';
		for (int i=0;i<s.length();i++)
			if (s[i]==c){
				res++;
				c = sum-c;
			}
		cout << "Case #" << tc << ": " << res << endl;
	}

	return 0;
}