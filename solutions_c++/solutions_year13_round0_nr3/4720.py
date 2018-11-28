#include <stdio.h>
#include <stdlib.h>
#include <string.h>
unsigned long start = 1; 
unsigned long end = 10000000 ; 
char buffer[1024];
unsigned long long prepare[1024];
int idx = 0; 

bool isParlin()
{
	int size ;
	size = strlen(buffer) ; 
	if ( size == 1 ) 
		return true;
	char *p , *q ;
	
	char *t;
	if ( size % 2 == 0 )
	{
		p = buffer ;
		q = p + ( size /2 ) ; 	
		t = q -1 ;
			
	}else {
		p = buffer ;
		q = p + ( size /2 ) + 1 ; 
		t = q - 2; 	

	}
	while ( t >= p ) 
		{
			if ( *t != *q )
				return false;
			--t;
			++q; 
		}

	return true;
}

bool isParlin2(unsigned long long i)
{
	char buf[256];
	sprintf(buf, "%lld" ,i ) ; 
	int size ;
	size = strlen(buf) ; 
	if ( size == 1 ) 
		return true;
	char *p , *q ;
	
	char *t;
	if ( size % 2 == 0 )
	{
		p = buf ;
		q = p + ( size /2 ) ; 	
		t = q -1 ;
			
	}else {
		p = buf ;
		q = p + ( size /2 ) + 1 ; 
		t = q - 2; 	

	}
	while ( t >= p ) 
		{
			if ( *t != *q )
				return false;
			--t;
			++q; 
		}

	return true;
}


int precalc()
{
	unsigned long i; 	
	unsigned long long mul;
	for ( i = start ; i <= end ; i ++ )
	{
		sprintf(buffer, "%lu", i ) ; 	
		bool ok = isParlin() ; 
		if ( ok == true ) {
			//printf("%s\n" , buffer ) ; 
			
			mul = (unsigned long long ) i * (unsigned long long)i ; 	
			bool sol = isParlin2(mul) ;
			if ( sol == true ) {
				//printf("%s %lld \n" ,buffer,  mul ) ; 		
				prepare[idx++] = mul ; 
			}
		}

	}
	
	return 0;
}

int main()
{
	precalc();
	int cnt;
	scanf("%d" ,&cnt) ; 
	for ( int i = 0 ; i < cnt ; i ++ )
	{
		unsigned long long start , end ; 
		int z=-1;
		scanf("%lld %lld" , &start,&end) ; 
		//printf("%lld %lld\n" , start, end ) ; 
		for ( int j = 0 ; j < idx ; j ++ )
		{
			if ( z == -1 && start <= prepare[j]  )
				z = 0 ;

			if ( end < prepare[j] ) 
			{
				break;
			}	
			else 
			{
				if ( z>= 0 )
					++z;
			}
		}
		if ( z== -1 )
			z = 0 ; 
		printf("Case #%d: %d\n" , i+1 ,z ) ; 
	}

	return 0;
}

