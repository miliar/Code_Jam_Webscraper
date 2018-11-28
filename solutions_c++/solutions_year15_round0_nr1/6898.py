#include <iostream>
#include <string>

int main()
{
	unsigned int T, size;
	std::string str;
	std::cin >> T;
	for(int t=0; t<T; ++t){
		std::cin >> size >> str;
		int preSum=str[0]-'0';
		int r=0;
		for(int i=1; i<=size; ++i){
			if(str[i] > '0' && preSum < i){
				r += i-preSum;
				preSum += (i-preSum);
			}
			preSum += str[i]-'0';
		}
		std::cout << "Case #" << t+1 << ": " << r << '\n';
	}
	return 0;
}