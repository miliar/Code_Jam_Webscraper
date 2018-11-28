#include <stdio.h>

int main(void) {

	int T,ar[4][4],suff_ar[4][4],row,suff_row,c,d,n=1;
	scanf("%d",&T);
	while(T--)
	{	
	scanf("%d",&row);
  	for( c = 1 ; c <= 4 ; c++ )
    {
      for( d = 1 ; d <= 4 ; d++ )
        {
          scanf("%d",&ar[c][d]);

        }

    }
    
    scanf("%d",&suff_row);
     for( c = 1 ; c <= 4 ; c++ )
    {
      for( d = 1 ; d <= 4 ; d++ )
        {
          scanf("%d",&suff_ar[c][d]);

        }

    }
    
    
    int check=0,flag,temp;
    flag=0;
    for( d = 1 ; d<=4 ; d++ )
      {
        	for( c = 1 ; c<=4 ; c++ )
        	{
          		if(ar[row][d]==suff_ar[suff_row][c])
				{	check++;
				if (check<2)
				temp=ar[row][d];
				}
      		}
      }
        	
    if (check>1)
    		printf("Case #%d: Bad magician!\n",n);
	if (check==0)
			printf("Case #%d: Volunteer cheated!\n",n);
	if(check==1)
			printf("Case #%d: %d\n",n,temp);  
			 n++;
	}
	return 0;
}
