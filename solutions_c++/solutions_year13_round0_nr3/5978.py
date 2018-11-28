#include <cstdio>
#include <cmath>
#include <string>
#include <sstream>

using namespace std;

bool isPalindrom(long int a){
	ostringstream ss;
	ss << a;
	string str = ss.str();
	long int len = str.length();
	for (long int i = 0;i<len/2 + 1;i++){
		if (str[i]!=str[len-i-1]) return false;
	}
	return true;
}

int main(){
	int z;
	scanf("%d",&z);
	for (int k=1;k<=z;k++){
		long int A,B;
		int counter = 0;
		scanf("%ld %ld",&A, &B);
		for (long int i=(int)sqrt(A);i<=sqrt(B) +1;i++){
			if (isPalindrom(i)){
				long int sq = i * i;
				if (sq <= B && sq>=A && isPalindrom(sq)) {
					counter++;
				}
			}
			
		}
		printf("Case #%d: %d\n",k,counter);
	}
	return 0;
}
