// code jam 2016 problem 1
//

#include <stdio.h>

int getSheeps(int sheep)
{
	if (sheep == 0){
		return sheep;
	}

	int total = 0;
	bool seen[10] = { false, false, false, false, false, false, false, false, false, false };
	bool seenAll = false;

	while (!seenAll) {
		int next = total + sheep;

		while (next) {
			seen[next % 10] = true;
			next = next / 10;
		}

		seenAll = true;
		for (int i = 0; i < 10; i++){
			if (!seen[i]) {
				seenAll = false;
				break;
			}
		}

		total += sheep;
	}

	
	
	return total;
}

int main(int argc, char ** argv)
{
	int n;

	scanf_s("%d", &n);
	int sheeps[100];


	for (int i = 0; i < n; i++) {
		scanf_s("%d", sheeps + i);
	}

	for (int i = 0; i < n; i++) {
		int result = getSheeps(sheeps[i]);
		printf("Case #%d: ", i+1);

		if (result) {
			printf("%d\n", result);
		} else {
			printf("INSOMNIA\n");
		}
	}

	return 0;
}

