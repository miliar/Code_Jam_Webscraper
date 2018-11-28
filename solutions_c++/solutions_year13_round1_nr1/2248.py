#include<stdio.h>
#include<math.h>

__int64 getSolution(double a,double b,double c ,int selection)
{
	if(selection==1)
	{
		return (-b + sqrt(b*b-4*a*c))/(2*a) ;
	}
	else
	{
		return (-b - sqrt(b*b-4*a*c))/(2*a) ;
	}
}

__int64 max(__int64 a,__int64 b)
{
	return a>b?a:b ;
}

double a,b,c,t,r;
int main()
{
	freopen("A-small-attempt0.in","r",stdin) ;
	freopen("A-small-attempt0.out","w",stdout) ;
	int T ; scanf("%d" , &T) ;
	int cases = 1;
	
	while(T--)
	{
		__int64 count = 1;
		scanf("%lf %lf",&r,&t) ;
		a = 2 ;
		b = 2*r+3 ;
		c = 2*r+1-t ;
		__int64 s1=  getSolution(a,b,c,0) ;
		__int64 s2= getSolution(a,b,c,1) ;
		
		if(s1<0) s1=0 ; 
		if(s2<0) s2=0 ;
		//printf("s1:%I64d s2:%I64d\n",s1,s2) ;
		
		count += max(s1,s2) ;
		printf("Case #%d: %I64d\n",cases++,count) ;
	}
	return 0 ;
}
