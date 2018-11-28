#include <cstdio>
#include <cmath>

using namespace std;

int main() 
{        
        freopen("D-small-attempt2.in", "r", stdin);
        freopen("D-small-attempt2.out", "w", stdout);
        int t,x,r,c,m=0;
        scanf("%d",&t);
		
		while(t>0)
		{
			m++;
			scanf("%d %d %d",&x,&r,&c);
			if(((r*c)%x) !=0)
			printf("Case #%d: RICHARD\n",m);
	
			else 
				{
				  if(x==4 && r*c==8)
			       	printf("Case #%d: RICHARD\n",m);
				  else{
    				if( (x>2 )&& (r==1 || c==1 || (r*c==x)) ) 
     				printf("Case #%d: RICHARD\n",m);
 			       	else
				printf("Case #%d: GABRIEL\n",m);
				  }
				}
			t--;
    	}
		return 0;
	}
