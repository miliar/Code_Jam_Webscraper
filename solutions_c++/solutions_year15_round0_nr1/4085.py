#include<stdio.h>
#include<iostream>

using namespace std;

const int MAX = 1002;

int main(){
	int number;
	int t;
	int smax;
	char ch[MAX];
	int shyness[MAX];
	int temp;
	int answer;

	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &t);
	number = 0;
	while (t--){
		number++;
		scanf("%d%s", &smax, ch);
		for (int i = 0; i <= smax; i++){
			shyness[i] = ch[i] - '0';
		}
		
		answer = 0;
		temp = shyness[0];
		for (int j = 1; j <= smax; j++){
			if (shyness[j] != 0){
				if (temp < j){
					answer += j - temp;
					temp = j;
				}
				temp += shyness[j];
			}
		}
		printf("Case #%d: %d\n", number, answer);
	}


	return 0;

}



