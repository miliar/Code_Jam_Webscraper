#include <cstdio>
#include <cmath>
using namespace std;
int main(void) {
          freopen("A-small-attempt1.in", "r", stdin);
	  freopen("A-small-attempt1.out", "w", stdout);

	int n,m=0,a,s,s_max,i,extra,j;
	scanf("%d",&n);
	while(n>0)
	{   m++;
		scanf("%d",&s_max);
		extra=0;
		s=0, j=0; 
		scanf("%d",&a);
		if( s_max >0)
		{  
		    i=pow(10,s_max);
		    while(i>=10)
		    {   j++;
		    	s+=a/i;
		    	a=a%i;
		    	i/=10;
			if(j>s)
			{extra++; 
			s++;}
		    }
		    
		}
		printf("Case #%d: %d\n",m,extra);
		n--;
	}
	
	return 0;
}
