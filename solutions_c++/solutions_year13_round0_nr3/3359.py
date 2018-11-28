#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>
#include <cmath>
bool isPalindrome(long num){
    std::ostringstream os;
    os << num;
    std::string str =os.str();
    int len = str.length();
    for(int j=0; j < len/2; ++j){
	if(str[j]!=str[len-1-j]) return false;
    }
    return true;
}
int main(void){
    int T,res=0;
    long A,B,temp,square;
    std::cin >> T;
    for(int i=0; i<T; ++i){
	std::cin >> A >> B;
	temp = sqrt(A);
	if(temp*temp < A) temp += 1;
	square = temp*temp;
	while(square <= B){
	    if(isPalindrome(temp) && isPalindrome(square))
		res++;
	    temp = temp + 1;
	    square = temp * temp;
	}
	std::cout << "Case #" << i+1 << ": " << res << std::endl;
	res = 0;
    }
}

