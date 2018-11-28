#include <stdio.h> 
#include <iostream> 
#include <memory.h> 
#include <assert.h> 
#include <algorithm> 
#include <functional> 
#include <vector> 
#include <string> 
#include <map> 
#include <set> 
#include <deque> 
#include <math.h> 
#include <string> 
#include <math.h> 


using namespace std;
void FindWinner(int x,int r,int c,int t)
{
       	int p; 
	if(r>c)
        {
            int z;
	    z=r;
            r=c;
            c=z;
        }
        p=r*c;
        if(x==1)
	{
         printf("Case #%d: GABRIEL\n",t);
	}
        else if(x==2)
        {
            if((r>1||c>1)&&p%x==0)
	    {
                printf("Case #%d: GABRIEL\n",t);
	    }
                else
	    {
                printf("Case #%d: RICHARD\n",t);    
	    }
        }
        else if(p%x!=0||x>=(2*r+1)||(x>=(c+r-2)&&x>3))
	{
            printf("Case #%d: RICHARD\n",t);
        }
        else if(x>r&&x>c)
	{
            printf("Case #%d: RICHARD\n",t);
        }
        else
	{
	printf("Case #%d: GABRIEL\n",t);
	}

}
int main()
{
	int t,T;
	freopen( "input.txt", "r", stdin );
    	freopen( "output.txt", "w", stdout );
	
	cin >> T;
	for(int t=1;t<=T;t++)
	{
		int a,b,c;
		cin >> a >> b >> c;
		FindWinner(a,b,c,t);
	}
	return 0;
}

