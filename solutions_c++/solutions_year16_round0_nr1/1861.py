#include <iostream>
#include <string>
#include <stdio.h>

int T;

using namespace std;
int main(){
	scanf("%d", &T);
	for(int i = 0; i < T; i ++){
		int N;
		scanf("%d", &N);
		bool contain[10];
		for(int zz = 0; zz < 10; zz ++)
			contain[zz] = false;
		bool end = false;
		long num = 0;
		if(N == 0){
			printf("Case #%d: INSOMNIA\n", i+1);
		}
		else{
			while(end == false){
				num += N;
				long temp = num;
				while(temp != 0){
					int digit = temp % 10;
					contain[digit] = true;
					temp /= 10;
				}
				end = true;
				for(int z = 0; z < 10; z ++){
					if(contain[z] == false)
						end = false;
				}
			}
			printf("Case #%d: %d\n", i+1, num);
		}
	}
}