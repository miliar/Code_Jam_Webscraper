#include<stdio.h>
#include<iostream>

using namespace std;

int main(){
	int number;
	int t;
	int x;
	int r;
	int c;
	int answer;

	freopen("D-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &t);

	number = 0;
	while (t--){
		number++;
		scanf("%d%d%d", &x, &r, &c);
		if (r * c % x != 0){
			answer = 0;
		}
		else{
			if (x >= 7){
				answer = 0;
			}
			else if (x == 1){
				answer = 1;
			}
			else if (x == 2){
				answer = 1;
			}
			else if (x == 3){
				if (r * c >= 6){
					answer = 1;
				}
				else{
					answer = 0;
				}
			}
			else if (x == 4){
				if (r <=2 || c <= 2){
					answer = 0;
				}
				else{
					answer = 1;
				}
			}
			else if (x == 5){
				if (r <= 2 || c <= 2){
					answer = 0;
				}else if (r >= 4 && c >= 4){
					answer = 1;
				}
				else if (r == 3 || c == 3){
					if (r > 5 || c > 5){
						answer = 1;
					}
					else{
						answer = 0;
					}
				}
			}
			else if (x == 6){
				if (r <= 3 || c <= 3){
					answer = 0;
				}
				else{
					answer = 0;
				}
			}
		}
		if (answer == 1){
			printf("Case #%d: GABRIEL\n", number);
		}
		else{
			printf("Case #%d: RICHARD\n", number);
		}

	}




	return 0;

}



