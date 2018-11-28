// code jam 2016 problem 2
//

#include <stdio.h>
#include <stdlib.h>

#define MAX 100

typedef struct stack {
	bool data[MAX];
	int len;
} Stack;

int s_flip(Stack * s, int pos){
	if (pos > s->len){
		pos = s->len; // sanity check
	}

	bool rev[MAX];

	for (int i = 0; i < pos; i++){
		rev[i] = !s->data[i]; // negate values on top of stack
	}

	for (int i = 0; i < pos; i++){
		s->data[i] = rev[pos - i - 1]; // put back in reverse order
	}
	
	return 1;
}

int s_reduce(Stack * s){
	int count = 0;

	//start at the end
	int pos = s->len;

	while (pos > 0){
		if (s->data[pos - 1]){ //if last item is correct, nothing is needed further
			pos -= 1; 
		}
		else {
			if (!s->data[0]){ // if last item and first item are wrong, flip the entire stack
				count += s_flip(s, pos);
			}
			else { // else find the first _correct_ value up the stack and flip there
				int subPos = pos;
				while (!s->data[subPos - 1]){
					subPos -= 1;
				}
				count += s_flip(s, subPos);
			}
		}
	}


	return count; 
}

int main(int argc, char ** argv)
{
	int n;

	scanf_s("%d", &n);
	Stack * stacks[100];


	for (int i = 0; i < n; i++) {
		stacks[i] = (Stack *)malloc(sizeof(Stack));
		stacks[i]->len = MAX;

		char stack[MAX + 1];
		scanf_s("%s", stack, MAX + 1);

		for (int j = 0; j < MAX; j++){
			char c = stack[j];

			switch (c) {
				case '+':
					stacks[i]->data[j] = true;
					break;
				case '-':
					stacks[i]->data[j] = false;
					break;
				default:
					stacks[i]->len = j;
					j = MAX; //skip to end of loop, we're done
					break;
			}
		}
	}

	for (int i = 0; i < n; i++) {
		printf("Case #%d: %d\n", i+1, s_reduce(stacks[i]) );

		free(stacks[i]);
	}

	return 0;
}

