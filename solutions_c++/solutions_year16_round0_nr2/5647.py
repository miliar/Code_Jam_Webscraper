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
	printf("Case #%d: %d\n", test, numb);
}

int main(){

#ifdef _CONSOLE
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif

	int count_test;
	cin>>count_test;

	for(int test = 1; test <= count_test; test++){
		string str;
		cin>>str;
		str += "+";

		int res = 0;
		while(1){
			bool check = true;

			for(int i=0; i<str.size() - 1; i++){
				if(str[i] != str[i + 1]){
					check = false;
					for(int j=0; j<=i; j++){
						if(str[j] == '+'){
							str[j] = '-';
						}
						else{
							str[j] = '+';
						}
					}
					break;
				}
			}

			if(check){
				break;
			}

			res++;
		}


		print(test, res);
	}


	
	return 0;
}

