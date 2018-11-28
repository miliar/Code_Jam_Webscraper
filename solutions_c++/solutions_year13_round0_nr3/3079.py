#include <stdio.h>

//"cheat" method
//palindromes that are sqare numbers from 1 - 1000
//1 4 9 121 484 676
//only 676's square root is not a sqaure of a palindrome
//thus, for the small dataset the answers are really easy
//there are only 1 4 9 121 484 that are fair and square numbers
//thus just looking at the limits given gives the answer
//a max of 5


int main()
{
    int T, C;
	int A, B;
	int total;

    scanf("%i\n", &T);

    for (C = 1;C <= T;C++)
    {
		total = 5;//reset result
        scanf("%i %i\n", &A, &B);
		
		if (A > 1) total--;
		if (A > 4) total--;
		if (A > 9) total--;
		if (A > 121) total--;
		if (A > 484) total--;
		
		if (B < 1) total--;
		if (B < 4) total--;
		if (B < 9) total--;
		if (B < 121) total--;
		if (B < 484) total--;
		
		

        printf("Case #%i: %i\n", C, total);

    }

    return 0;
}
