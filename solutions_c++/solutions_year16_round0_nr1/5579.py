#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <unordered_map>
#include <unordered_set>

using namespace std;
typedef long long ll;

vector<char> used;

void print(int test, int numb){
	if(numb == -1){
		printf("Case #%d: INSOMNIA\n", test);
	}
	else{
		printf("Case #%d: %d\n", test, numb);
	}
}

int main(){

#ifdef _CONSOLE
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif

	int count_test;
	cin>>count_test;

	for(int test = 1; test <= count_test; test++){
		int n;
		cin>>n;
		if(n == 0){
			print(test, -1);
			continue;
		}
		used.assign(10, false);
		int cnt = 1;
		while(1){
			int m = cnt * n;
			while(m){
				int numb = m % 10;
				used[numb] = 1;
				m /= 10;
			}

			bool check = true;
			for(int i=0; i<10; i++){
				if(!used[i]){
					check = false;
					break;
				}
			}

			if(check){
				break;
			}			
			cnt++;
		}

		print(test, n * cnt);
	}


	
	return 0;
}

