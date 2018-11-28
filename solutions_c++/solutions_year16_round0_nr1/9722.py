#include <stdio.h>

int main(){

	int n, t;

	scanf("%i", &t);
	
	for (int b = 1; b <= t; b++)
	{
		scanf("%i", &n);
		bool seenDigits[10] = {false,false,false,false,false,false,false,false,false,false};

		for (int a = 1; a <= 1000; a++)
		{
			int numb = a * n;				

			while (numb > 0)
			{
				int dig = numb % 10;
				numb = numb / 10;
				
				seenDigits[dig] = true;
			}

			bool ok = true;			

			for(int i = 0; i < 10; i++)
			{
				if (!seenDigits[i])
				{
					ok = false;
					
					break;
				} 
			}

			if (ok) 
			{
				printf("Case #%i: %i\n", b, a * n);
				break;
			}
			else if (a == 999){
				printf("Case #%i: INSOMNIA\n", b);		
			}
		}

	}

	return 0;
}
