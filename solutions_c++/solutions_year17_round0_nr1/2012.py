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

int func(string str, int k){
	int count = 0;
	for(int i=0; i<str.size(); i++){
		if(str[i] == '+'){
			continue;
		}
		count++;
		for(int j=i, p=0; p<k; p++, j++){
			if(j >= str.size()){
				return -1;
			}
			if(str[j] == '-'){
				str[j] = '+';
			}
			else{
				str[j] = '-';
			}
		} 
	}
	return count;
}

int main(){

#ifdef _CONSOLE
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif

	int countTest;
	cin>>countTest;	
	for(int test = 1; test <= countTest; test++){
		string str;
		int k;
		cin>>str>>k;

		int count = func(str, k);

		if(count == -1){
			printf("Case #%d: IMPOSSIBLE\n", test);
		}
		else{
			printf("Case #%d: %d\n", test, count);
		}

		cerr<<test<<"\n";
	}
	
	return 0;
}

