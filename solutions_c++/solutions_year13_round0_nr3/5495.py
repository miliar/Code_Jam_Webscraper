// Brute force for 10p!

#include <math.h>
#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <vector>
#include <set>
#include <string>
#include <sstream>

using namespace std;

bool is_palindrome(int n) {
	ostringstream ss;	
	ss << n;
	string numstring(ss.str());
	int l = numstring.length();
	
	for (int i=0; i<numstring.length() / 2; i++) {	
		if (numstring[i] != numstring[l - i - 1])
			return false;
	}
	
	return true;	
}

bool is_perfect_fair(int n) {	
	if (is_palindrome(n)) 
		return is_palindrome(n*n);
		
	return false;
}

int main(){
	int from, to, n;
	
	int pfn=0;
	cin >> n;
	
	for (int casen=1; casen<=n; casen++) {
		pfn=0;
		cin >> from >> to;
	
		for (int i=sqrt(from); i<sqrt(to)+1; i++) {
			if (from <= i*i && i*i <= to) {
				if (is_perfect_fair(i)) 				
					pfn++;
			}
		}
		cout << "Case #" << casen << ": " << pfn << endl;
	}

	return 0;
	
}
	
	
