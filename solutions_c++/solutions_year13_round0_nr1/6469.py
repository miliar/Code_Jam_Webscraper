#include<cstdio>


int masks[] = { 15, 240, 3840, 61440, 34952, 17476, 8738, 4369, 33825, 4680 };

int main()
{
	freopen("input","r",stdin);
	freopen("output","w",stdout);
	
	char ch;
	int T, hashX, hashO;
	
	scanf("%d",&T);
	
	int k = 1;
	while( T-- )
	{
		scanf("\n");
		printf("Case #%d: ",k++);
	
		hashX = hashO = 0;	
		int p = 0;
		for( int i = 0, j = -1; i < 20; ++i )
		{
			scanf("%c",&ch);
			if( ch != '\n' ) ++j;
			
			if( ch == 'X' || ch == 'T' ){
				hashX |= (1<<j);
//				printf("|%d| X\n",j);
			}
			
			if( ch == 'O' || ch == 'T' ){
				hashO |= (1<<j);
//				printf("|%d| O\n",j);
			}	
				
			if( ch == '.' ) ++p;
		}
		
//		printf("|%d %d %d|\n", hashX, hashO, p);
		
		bool win = false;
		for( int i = 0; i < 10; ++i )
		{
			if( (hashX & masks[i]) == masks[i] ){
//				printf("|%d| ", masks[i]);
				printf("X won\n"); 
				win = true;
				break;
			}
			
			if( (hashO & masks[i]) == masks[i] ){
//				printf("|%d| ", masks[i]);
				printf("O won\n"); win = true;
				break;
			}
		}
		
		if( win ) continue;
		
		if( !p ){
			printf("Draw\n");
			continue;
		}
		
		printf("Game has not completed\n");		
	}
		
	return 0;
}
