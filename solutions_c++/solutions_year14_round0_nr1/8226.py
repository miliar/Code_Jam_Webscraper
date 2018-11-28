#include<bits/stdc++.h>

using namespace std;

int main ()
{

	int n , m , t , i , j , k , ans , arr , count , state1[4] , state2[4];
	FILE *in , *out;
	
	in = fopen ("take.txt", "r");
	out = fopen ("output.txt", "w");
	
	fscanf(in , "%d", &t);
	
	for(k = 1; k <= t; k++)
	{
	
		fscanf(in , "%d", &n);
		
		for(i = 1; i <= 4; i++)
		{
			for(j = 1; j <= 4; j ++)
			{
				fscanf(in , "%d", &arr);
				
				if(i == n)
					state1[j - 1] = arr;
			}
		}
		
		fscanf(in , "%d", &m);
		
		for(i = 1; i <= 4; i++)
		{
			for(j = 1; j <= 4; j ++)
			{
				fscanf(in , "%d", &arr);
				
				if(i == m)
					state2[j - 1] = arr;
					
			}
			
		}
		
		count = 0;
		
		for(i = 0; i < 4; i++)
		{
			for(j = 0; j < 4; j++)
			{
				if(state1[i] == state2[j])
				{
					count ++;
					ans = state1[i];
				}
				
			}
			
		}
		
		if(count < 1)
			fprintf(out , "Case #%d: Volunteer cheated!\n", k);
			
		else if(count > 1)
			fprintf(out , "Case #%d: Bad magician!\n", k);
			
		else
			fprintf(out , "Case #%d: %d\n", k , ans);
			
	}
	
	return 0;
}
			
