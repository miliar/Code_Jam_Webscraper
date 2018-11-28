#include <stdio.h>
#include <stdlib.h>
#define MAX 1001
using namespace std;

int cases;
int n;
int ncase = 0;

int main() {
	scanf("%d\n",&cases);
	while( cases -- )
	{
		int ans = 0;
		int people = 0;
		char people_now = '\0';

		scanf("%d ",&n);

		for( int i=0; i <= n; i++ )
		{
			scanf("%c",&people_now);
			if( people < i ){
				ans+= i-people;
				people+=i-people;
			}
			people+=people_now-'0';			
		}	
		ncase++;
		printf("Case #%d: %d\n",ncase,ans);
	}	
	return 0;		
}