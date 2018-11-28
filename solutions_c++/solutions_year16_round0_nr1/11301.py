/*
* @Author: Lich_Amnesia
* @Date:   2016-04-09 15:34:47
* @Last Modified by:   Alwa
* @Last Modified time: 2016-04-09 15:41:35
*/

#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>

using namespace std;
int hash[10];
bool calc(int n){
	while(n){
		hash[n % 10] = 1;
		n /= 10;
	}
	for (int i = 0; i < 10; i ++){
		if (hash[i] == 0){
			return 0;
		}
	}
	return 1;
}

int main(){
	int T,t = 0,n;
	cin >> T;
	while (t ++ < T){
		cin >> n;
		int flag = 0;
		memset(hash,0,sizeof(hash));
		printf("Case #%d: ", t);
		for (int i = 1; i <= 1000; i ++){
			if (calc(n * i)){
				flag = 1;
				printf("%d\n", n * i);
				break;
			}
		}
		if (!flag)
			printf("%s\n", "INSOMNIA");
	}
    return 0;
}