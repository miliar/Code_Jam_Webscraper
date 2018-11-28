// A.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <vector>
using namespace std;
struct POS {int start; int end;};
int _tmain(int argc, _TCHAR* argv[])
{
	int T,n;
	string L;
	cin >> T;
	for (int iCase = 1; iCase <= T; iCase++) {
		cin >> L >> n;
		int count = 0;
		vector<POS> check;
		POS p;
		p.start = p.end = -1;
		for (int i = 0; i <= L.size(); i++) {
			if (i == L.size() || L[i] == 'a' || L[i] == 'e' || L[i] == 'i' || L[i] == 'o' || L[i] == 'u') {
				if (p.start != -1) {
					p.end = i - 1;
					if (p.end - p.start + 1 >= n) {
						POS newP;
						newP = p;
						check.push_back(newP);
						
					}
					p.start = p.end = -1;
				}
			} else {
				if (p.start == -1)
					p.start = i;
			}
		}
		for (int i = 0; i < L.size(); i++) {
			for (int j = i + n - 1; j < L.size(); j++) {
				for (int s = 0; s < check.size(); s++) {
					if (i >= check[s].start && j <= check[s].end) {
						if (j - i + 1 >= n) {
							count++;
							break;
						}
					}
					if (i <= check[s].start && j >= check[s].end) {
						count++;
						break;
					} 
					if (check[s].start >= i && check[s].start <= j) {
						if (j >= check[s].end || j - check[s].start + 1 >= n) {
							count++;
							break;
						}
					} 
					if (check[s].end >= i && check[s].end <= j) {
						if (i <= check[s].start || check[s].end - i + 1 >= n) {
							count++;
							break;
						}
					}
				}
			}
		}
		cout << "Case #" << iCase << ": " << count << '\n';
	}
	
	return 0;
}

