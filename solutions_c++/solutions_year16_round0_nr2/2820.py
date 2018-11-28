#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <utility>
#include <bitset>

using namespace std;

int main(){
	int T;
	cin >> T;
	for (int test = 0; test < T; test++){
		string line;
		cin >> line;
		int count = 0;
		int todo = line.size() - 1;
		while (todo >= 0){
			if (line[todo] == '-'){
				for (int i = 0; i <= todo; i++)
					if (line[i] == '+')
						line[i] = '-';
					else
						line[i] = '+';
				count++;
			}
			todo--;
		}
		printf("Case #%d: %d\n", test + 1, count);
	}
}
