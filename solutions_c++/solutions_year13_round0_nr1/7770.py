#include <iostream>
#include <cstdio>
using namespace std;

int main() 
{
    char a[4][4] ;
    int c=1, n, t ;
    cin>>n ;
    
    while(n)
    {
        bool done = false, fre=false ,O=false, X=false ;
        
        //Input
        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
                cin>>a[i][j] ;
                
        //Horizontal
        for(int i=0; i<4; i++)
        {
    		bool cont = false ;
			
            for(int j=0; j<4; j++)
                if (a[i][j]=='.')   
                {done = false ;  fre = cont = true ; break ;}
                
            if (cont) 
			{cont = false ;	continue ;}
			
            t = a[i][0]+a[i][1]+a[i][2]+a[i][3] ;
            
            if ((t%79 == 0) || ((t-84)%79==0))
                {done = O = true ;   break;}
            else if ((t%88 == 0) || ((t-84)%88==0))
                {done = X = true ;   break;}
        }
              
        //Vertical
        if (!done)
        for(int j=0; j<4; j++)
        {
			bool cont = false ;
			
            for(int i=0; i<4; i++)
                if (a[i][j]=='.')  
                    {done = false ;  fre = cont = true ; break ;}
            
			if (cont) 
			{cont = false ;	continue ;}
			
            t = a[0][j]+a[1][j]+a[2][j]+a[3][j] ;
            
            if ((t%79 == 0) || ((t-84)%79==0))
                {done = O = true ;   break;}
            else if ((t%88 == 0) || ((t-84)%88==0))
                {done = X = true ;   break;}
        }
        
        //Diagonal
        if (!done)
        {
            //Left to Right
            if ((a[0][0]*a[1][1]*a[2][2]*a[3][3])%46 != 0)
            {
                t = a[0][0]+a[1][1]+a[2][2]+a[3][3] ;
            
                if ((t%79 == 0) || ((t-84)%79==0))
                    done = O = true ;
                else if ((t%88 == 0) || ((t-84)%88==0))
                    done = X = true ;
            }
        }   
        
        if (!done)
        {
            //Right to Left
            if ((a[0][3]*a[1][2]*a[2][1]*a[3][0])%46 != 0)
            {
                t = a[0][3]+a[1][2]+a[2][1]+a[3][0] ;
            
                if ((t%79 == 0) || ((t-84)%79==0))
                    done = O = true ;
                else if ((t%88 == 0) || ((t-84)%88==0))
                    done = X = true ;
            }
        }
    
                if (X)
                    printf("Case #%d: X won\n", c);
                else if (O)
                    printf("Case #%d: O won\n", c);
                else if (fre)
                    printf("Case #%d: Game has not completed\n",  c);
                else
                    printf("Case #%d: Draw\n",  c); 
                
            
        c++ ;
        n-- ;
    }
	return 0;
    
}