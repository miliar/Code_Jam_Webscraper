#include <stdio.h>
#include <string.h>

void doSwift(bool *stack, int swift){
	bool aux[110];
	for (int i = 0; i <= swift; i++)
		aux[swift - i] = !stack[i];
	for (int i = 0; i <= swift; i++)
		stack[i] = aux[i];
}

int main(){
	int cases, size, swift, moves;
	bool stack[110], done;
	char input[110];
	scanf("%d", &cases);
	for (int c = 1; c <= cases; c++){
		scanf("%s", input);
		size = strlen(input);
		for (int i = 0; i < size; i++){
			if (input[i] == '+')
				stack[i] = true;
			else if(input[i] == '-')
				stack[i] = false;
		}
		moves = 0;
		done = false;
		while(!done){
			swift = -1;
			while (swift < size - 1 && stack[swift + 1])
				swift++;
			if (swift == size - 1)
				done = true;
			else if (swift >= 0){
				moves++;
				doSwift(stack, swift);
			}
			else if(swift == -1){
				swift = size - 1;
				while (swift >= 0 && stack[swift])
					swift--;
				moves++;
				doSwift(stack, swift);
			}
		}
		printf("Case #%d: %d\n", c, moves);
	}
	return 0;
}