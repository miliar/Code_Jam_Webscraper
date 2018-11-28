#include<stdio.h>
#include<string.h>
__int64 A,B ;

int isP(__int64 n)
{
	char s[101] ;
	
	sprintf(s,"%I64d",n) ;
	//printf("") ;
	int h=0,t=strlen(s)-1 ;
	
	while(h<t){
		if(s[h] != s[t])return 0 ;
		h++;t--;
		}
	return 1 ;
}
int AB(__int64 n)
{
	if(n>=A && n<=B)return 1 ;
	return 0 ;
}

int main()
{
	int cases = 1;
	//freopen("C-small-attempt0.in","r",stdin) ;
	//freopen("C-small-attempt0.out","w",stdout) ;
	int t ; scanf("%d" , &t) ;
	while(t--)
	{
		scanf("%I64d %I64d",&A,&B) ;
		
		__int64 i=1; 
		__int64 count = 0 ;
		while(i*i <= B)
		{
			if(isP(i) && AB(i*i) && isP(i*i))	count++ ;
			i += 1 ;
		}
		printf("Case #%d: %I64d\n",cases++,count) ;
	}
	return 0 ;
}
/*
3
1 4
10 120
100 1000
*/
