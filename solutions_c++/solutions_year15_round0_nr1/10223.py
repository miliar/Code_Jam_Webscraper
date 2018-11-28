#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

int main() {
	int T, max_shyness, friends_count, current_standing;
	string input_str;
	scanf("%d", &T);
	int test_count=0;
	while(T--){
		test_count++;
		friends_count = 0;
		current_standing = 0;
		scanf("%d", &max_shyness);
		cin>>input_str;
		for(int i=0; i<=max_shyness; i++){
			int k = input_str[i] - '0';
			if(current_standing >= i){
				current_standing += k;
			}
			else{
				if(k > 0){
					friends_count += i-current_standing;
					current_standing += (k+i-current_standing);
				}
			}
		}
		
		printf("Case #%d: %d\n", test_count, friends_count);
	}
	return 0;
}