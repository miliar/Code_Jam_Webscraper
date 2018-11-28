#include <iostream>
#include <string>
using namespace std;

bool check(long long n);

int main() {

	freopen("C-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);

    int cases;
	cin >> cases;
	for(int i = 0; i < cases; i++) {
		long long lBound, rBound, result = 0;
		cin >> lBound >> rBound;
		for(int k = lBound; k <= rBound; k++) {
			bool temp = check(k);
			if(temp) result++;
		}
		cout << "Case #" << i+1 << ": " << result << endl;
	}
    return 0;  
}

bool check(long long n) {
	char s[105];
	itoa(n, s, 10);
	int len = strlen(s);
	for(int i = 0; i <=  (len/2)-1; i++) {
		if(s[i] != s[len-1-i])
			return false;
	}
	
	long long temp = sqrt(n);
	if(temp*temp == n)
	{
		// check palindrome of temp
		itoa(temp, s, 10);
		len = strlen(s);
		for(int i = 0; i <=  (len/2)-1; i++) {
		if(s[i] != s[len-1-i])
			return false;
		}
		return true;
	}
	else
		return false;
}