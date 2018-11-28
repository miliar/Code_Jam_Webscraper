#include<stdio.h>

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,o=0;
	scanf("%d", &t );
	while ( t-- )
	{
		int x, y,a[10],b[10],l1=0,l2=0,c[10],l=0;
		scanf("%d", &x);
		for ( int i = 1; i <= 4; i++ )
		{
			for ( int j = 1; j <= 4; j++ )
			{
			scanf("%d", &y );
			if ( i == x )
			a[l1++]=y;
			}
		}
		scanf("%d", &x);
		for ( int i = 1; i <= 4; i++ )
		{
			for ( int j = 1; j <= 4; j++ )
			{
			scanf("%d", &y );
			if ( i == x )
			b[l2++]=y;
			}
		} 
		for (int i = 0; i < l1; i++ )
		{
			for (int j = 0; j < l2; j++ )
			{
				if ( a[i] == b[j] )
				c[l++]=a[i];
			}
		}
		printf("Case #%d: ",++o);  
		if ( l == 1 )
		printf("%d\n",c[0]);
		else if ( l > 1 )
		puts("Bad magician!");
		else
		puts("Volunteer cheated!"); 
	}
}
