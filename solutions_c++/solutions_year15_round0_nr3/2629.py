#include<stdio.h>
#include<iostream>

using namespace std;

const int MAX = 10020;

int main(){
	int number;
	int t;
	char ch[MAX];
	int l;
	int x;
	int left;
	int right;
	int signleStr;
	int sign;
	int answer;
	int lcount;
	int rcount;
	int find;
	int cur;
	int mul[5][5] = { {0, 0, 0, 0, 0}, { 0, 1, 2, 3, 4 }, { 0, 2, -1, 4, -3 }, { 0, 3, -4, -1, 2 }, { 0, 4, 3, -2, -1 } };

	freopen("C-small-attempt3.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &t);

	number = 0;
	while (t--){
		number++;
		scanf("%d%d", &l, &x);
		scanf("%s", ch);

		answer = 0;
		sign = 1;
		left = ch[0] - 'i' + 2;
		for (int i = 1; i < l; i++){
			right = ch[i] - 'i' + 2;
			left = mul[left][right];
			if (left < 0){
				left = -left;
				sign *= -1;
			}
		}
		signleStr = left * sign;
		if ((signleStr == -1 && x % 2 == 1) || (signleStr >= 2 && x % 4 == 2) || (signleStr <= -2 && x % 4 == 2)){

			find = 0;
			lcount = 1;
			sign = 1;
			left = ch[0] - 'i' + 2;
			cur = 0;
			if (left != 2){
				for (int i = 1; i < 4 * l + 2; i++){
					lcount++;
					cur++;
					if (cur == l){
						cur = 0;
					}
					right = ch[cur] - 'i' + 2;
					left = mul[left][right];
					if (left < 0){
						left = -left;
						sign *= -1;
					}
					if (left * sign == 2){
						find = 1;
						break;
					}
				}
			}
			else{
				find = 1;
			}

			if (find == 0 || lcount > l * x){
				answer = 0;
			}
			else{
				find = 0;
				rcount = 1;
				sign = 1;
				right = ch[l - 1] - 'i' + 2;
				cur = l - 1;
				if (right != 4){
					for (int i = 1; i < 4 * l + 2; i++){
						rcount++;
						cur--;
						if (cur == -1){
							cur = l - 1;
						}
						left = ch[cur] - 'i' + 2;
						right = mul[left][right];
						if (right < 0){
							right = -right;
							sign *= -1;
						}
						if (right * sign == 4){
							find = 1;
							break;
						}
					}
				}
				else{
					find = 1;
				}

				if (find == 0 || lcount + rcount >= l * x){
					answer = 0;
				}
				else{
					answer = 1;
				}
			}
		}
		else{
			answer = 0;
		}
		if (answer == 1){
			printf("Case #%d: YES\n", number);
		}
		else{
			printf("Case #%d: NO\n", number);
		}

	}




	return 0;

}



