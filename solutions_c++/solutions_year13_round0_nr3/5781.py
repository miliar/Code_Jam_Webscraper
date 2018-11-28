#include <iostream>
#include <cmath>
#include <sstream>

using namespace std;

bool isPalindrome(int i){
	stringstream ss;
	ss << i;
	string s = ss.str();
	int l = s.length()-1;
	bool p = true;
	for (int j=0;j<l/2+1;j++)
		p = p && (s[j]==s[l-j]);
	return p;
}

int main() {
	int T,count;
	unsigned long A,B,a,b;
	cin >> T;

	for (int t=0;t<T;t++){
		cin >> A >> B;
		a = ceil(sqrt(A));
		b = floor(sqrt(B));
		count = 0;
		for (unsigned long i=a;i<=b;++i){
			if (isPalindrome(i) && isPalindrome(i*i))
				++count;
		}
		cout << "Case #" << t+1 << ": " << count << endl;
	}
	return 0;
}
