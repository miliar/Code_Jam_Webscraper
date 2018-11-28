#include<stdio.h>
#include<iostream>
#include<deque>
#include<string>


int main() {
	int tc;
	scanf("%d", &tc);
	for (int Tc = 1; Tc <= tc;Tc++) {
		std::string str;
		std::cin >> str;
		std::deque<char> deq;
		deq.push_back(str[0]);
		for (int i = 1; i < str.size(); i++) {
			if (deq.front() <= str[i]) {
				deq.push_front(str[i]);
			}
			else {
				deq.push_back(str[i]);
			}
		}
		printf("Case #%d: %s\n", Tc, std::string(deq.begin(),deq.end()).c_str());
	}
}