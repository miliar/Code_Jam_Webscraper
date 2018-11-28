#include <stdio.h>
int main()
{
	int previous[4], t, current[4], row, trg, i, j, k, tmp, pos;
	scanf("%d", &t);
	for( i = 0; i < t; i++) {
		scanf("%d", &row);
		for( j = 0; j < 4; j++)
		  for( k = 0; k < 4; k++) {
		  	scanf("%d", &tmp);
			if( j == row - 1)
			  previous[k] = tmp;
		  }
		scanf("%d", &trg);
		for( j = 0; j < 4; j++)
		  for(k = 0; k < 4; k++) {
			scanf("%d", &tmp);
			if( j == trg - 1)
			  current[k] = tmp;
		  }
		tmp = 0;
		for( j = 0; j < 4; j++)
		  for( k = 0; k < 4; k++)
			if( previous[j] == current[k]) {
			  tmp++;
			  pos = k;
			}
		if(tmp == 1)
		  printf("Case #%d: %d\n", i+1, current[pos]);
		else if( tmp > 1)
		  printf("Case #%d: Bad magician!\n", i+1);
		else if( tmp == 0)
		  printf("Case #%d: Volunteer cheated!\n", i+1);
	}
	return 0;
}
