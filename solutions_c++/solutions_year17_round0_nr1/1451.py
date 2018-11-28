// app.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <iostream>

int main()
{
		
		int count = 0;
		std::cin >> count;
		for (auto k = 0; k < count; ++k) {
			std::string S;
			int K = 0;
			std::cin >> S >> K;

			auto flip = [](std::string &S, size_t pos, size_t count) {
				for (auto n = pos; n < pos + count; ++n) {
					S[n] = S[n] == '+' ? '-' : '+';
				}
			};

			auto flips = 0;
			std::string value = "IMPOSSIBLE";
			while (true) {
				auto pos = S.find('-');
				if (pos == std::string::npos) {
					value = std::to_string(flips);
					break;
				}
				else if (pos + K <= S.length()) {
					flip(S, pos, K);
					flips += 1;
				}
				else {
					break;
				}
			}
			
			std::cout << "Case #" << (k + 1) << ": " << value << std::endl;
		}		
    return 0;
}

