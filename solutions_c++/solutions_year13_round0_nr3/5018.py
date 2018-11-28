#include <iostream>
#include <stdio.h>
#include <sstream>
#include <cmath>

using namespace std;

bool isPalindrome (int n){
    ostringstream os;
    os<<n;
    string s = os.str();
    int len = s.length();
    for (int i=0;i<len/2;i++)   if (s[i]!=s[len-i-1])   return false;
    return true;
}

int main (){
    int T, A, B, tcase = 1;
	scanf ("%d", &T);
	while (T--){
        scanf ("%d%d", &A, &B);
        int ret = 0;
        while (A<=B){
			int sqrtA = sqrt ((double)A);
            if (isPalindrome(A) && isPalindrome (sqrtA) && sqrtA*sqrtA == A)  ret++;
            A++;
        }
        printf ("Case #%d: %d\n", tcase++, ret);
	}
	return 0;
}