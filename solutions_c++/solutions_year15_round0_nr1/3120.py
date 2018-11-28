/*===============================================================
*   
*   FILE NAME:  qr-a.cpp
*   AUTHOR:     winoros
*   SHOOL:      BUPT
*   DATE:       04/11/2015 20:26:17
*   EMAIL:      winoros@gmail.com
*   Description:  
*
*
================================================================*/
#include <bits/stdc++.h>

int MAIN() {
	int n;
	std::string people;
	std::cin >> n >> people;
	int ans = 0, cnt = 0, len = people.length();
	for(int i = 0; i < len; ++i) {
		if(people[i] != '0'&& cnt < i) {
			ans += i - cnt;
			cnt += i - cnt;
		}
		cnt += people[i] -'0';
	}
	return ans;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int n;
	std::cin >> n;
	for(int i = 1; i <= n; ++i)
		std::cout << "Case #" << i << ": " << MAIN() << std::endl;
	return 0;
}
