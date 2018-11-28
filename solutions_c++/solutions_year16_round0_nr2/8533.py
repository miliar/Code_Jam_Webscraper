#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	int T;
	cin >> T;
	char ch;
	ch = getchar();	//Empty \n from buffer
	bool s[101];
	int count;
	int ans;
	int j;
	for(int k = 1; k <= T; k++) {
		ans = 0;
		count = 0;
		while((ch = getchar()) != '\n') {
			if(ch == '-') 
				s[count] = false;
			else 
				s[count] = true;
			count++;
		}
		/*******Turning initial conitguous minuses to pluses if any************/
		j = 0;
		while(j < count && s[j] == false){
			s[j] = true;
			j++;	
		}
		//printf("Value of j is %d\n", j);
		if(j > 0 ) ans++; //If any minuses were converted to pluses then incrment j;
		j = 0;
		while(j < count && s[j] ) j++; //Skip all pluses
		//printf("Value of j is %d\n", j);
			
		while(j != count) {		//i.e. while j doesn't reach the maximum value
			//algo to proceed
			while(j < count && s[j] == false){
				s[j] = true;
				j++;	
			}
			ans += 2;
			while(j < count && s[j] ) j++; //Skip all pluses
		}
		printf("Case #%d: %d\n", k, ans);
	}
	return 0;

}