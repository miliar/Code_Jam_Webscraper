#include <stdio.h>

int main(){

	int T, testcase = 1, input, count, i, temp, digit;
	int visited[10];

	FILE *finput = freopen("input.txt", "r", stdin);
	FILE *foutput = freopen("output.txt", "w+", stdout);

	scanf("%d", &T);

	while (T--){
		count = 0;
		for (i = 0; i < 10; i++){
			visited[i] = 0;
		}

		scanf("%d", &input);

		if (input == 0)
			printf("Case #%d: INSOMNIA\n", testcase++);
		else{
			i = 1;
			while (1){
				temp = input*(i++);
				while (1){
					digit = temp % 10;

					if (visited[digit] == 0){
						count++;
						visited[digit] = 1;
					}

					if (temp < 10)
						break;
					else temp /= 10;
				}
				if (count == 10) break;
			}
			printf("Case #%d: %d\n", testcase++, input*(i - 1));
		}
	}

	return 0;
}