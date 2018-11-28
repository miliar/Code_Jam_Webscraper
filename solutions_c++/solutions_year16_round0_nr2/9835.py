#include <cstdio>
#include <cstring>

void flipPile(char* pks, int len, int flipIndex){
	char pks2[len];

	for (int i = 0; i < len; i++){
		pks2[i] = pks[i];
	}
	for (int i = 0; i <= flipIndex; i++){
		pks[i] = (pks2[flipIndex - i]  == '+' ? '-' : '+');		
	}
}

int main(){

	int cases = 0;
	
	scanf("%i", &cases);

	for (int b = 1; b <= cases; b++)
	{
		char pkorder[100];
		scanf("%s", pkorder);

		int flipCount = 0;
		
		int pancakes = strlen(pkorder);
		
		char pks[pancakes];

		for (int i = 0; i < pancakes; i++){
			pks[i] = pkorder[i];					
		}

		char last = pks[0];
		for (int i = 0; i <= pancakes - 1; i++){
			if (pks[i] != last){
				flipPile(pks, pancakes, i - 1);
				flipCount++;	
				i = 0;
				last = pks[0];							
			}
			else if (pks[i] == '-' && i == pancakes - 1) {
				flipPile(pks, pancakes, i);
				flipCount++;	
			}
			last = pks[i]; 
		}	

		printf("Case #%i: %i\n", b, flipCount);
	}

	return 0;
}
