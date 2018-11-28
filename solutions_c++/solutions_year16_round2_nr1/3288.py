# include <iostream> 
# include <cmath>
# include <cstring>
# include <cstdio>
#include <stdlib.h> 

using namespace std ;


int compare (const void * a, const void * b)
{
    return ( *(int*)a - *(int*)b );
}

int min(int a , int b , int c)
{
    if( (a>=b && b>=c) || (b>=a && a>=c))
        return c ;
    else if ( (a >=c  && c >=b ) || (c >=a  && a >=b ))
        return b ;
    else
        return a ;
}


int main ()
{
    int x , i ;
    cin>>x ;
    for(i=0;i<x;i++)
    {
        int len , j , num=0 , temp , temp1 , temp2 ,  n[700] , nc=0 ;
        int count[27]={0} ;
        char a[2010] ;
        cin>>a ;
        len = strlen(a) ;
        for(j=0;j<len;j++)
        {
            count[(int)a[j]-64]++ ;

        }
        
        
        
        temp  = min(count[26] , count[5] , count[18]) ;
        if(temp>count[15])
            temp = count[15] ;
        if(temp>count[26])
            temp = count[26] ;
        if(temp>0)
        {
            num=num+temp ;
            count[26]-=temp ;
            count[5]-=temp ;
            count[18]-=temp ;
            count[15]-=temp ;
            for(j=0;j<temp;j++)
            {
                n[nc]=0 ;
                nc++;
            }
        }

        
        temp  = min(count[20] , count[23] , count[15]);
        if(temp>count[23])
            temp = count[23] ;
        if(temp>0)
        {
            num=num+temp ;
            count[20]-=temp ;
            count[23]-=temp ;
            count[15]-=temp ;
            for(j=0;j<temp;j++)
            {
                n[nc]=2 ;
                nc++;
            }

        }
        
        
        
        temp  = min(count[6] , count[15] , count[21]) ;
        if(temp>count[18])
            temp = count[18] ;
        if(temp>count[21])
            temp = count[21] ;

        if(temp>0)
        {
            num=num+temp ;
            count[6]-=temp ;
            count[15]-=temp ;
            count[21]-=temp ;
            count[18]-=temp ;
            for(j=0;j<temp;j++)
            {
                n[nc]=4 ;
                nc++;
            }

        }
        
        

        

        

        
        temp  = min(count[19] , count[9] , count[24]) ;
        if(temp>count[24])
            temp = count[24] ;
        if(temp>0)
        {
            num=num+temp ;
            count[19]-=temp ;
            count[9]-=temp ;
            count[24]-=temp ;
            for(j=0;j<temp;j++)
            {
                n[nc]=6 ;
                nc++;
            }

        }
        
        
        temp  = min(count[5] , count[9] , count[7]) ;
        if(temp>count[8])
            temp = count[8] ;
        if(temp>count[20])
            temp = count[20] ;
        if(temp>count[7])
            temp = count[7] ;
        if(temp>0)
        {
            num=num+temp ;
            count[5]-=temp ;
            count[9]-=temp ;
            count[8]-=temp ;
            count[7]-=temp ;
            count[20]-=temp ;
            for(j=0;j<temp;j++)
            {
                n[nc]=8 ;
                nc++;
            }

            
        }
        
        
        temp  = min(count[15] , count[14] , count[5]) ;
        if(temp>count[15])
            temp = count[15];
        if(temp>0)
        {
            num=num+temp ;
            count[15]-=temp ;
            count[14]-=temp ;
            count[5]-=temp ;
            for(j=0;j<temp;j++)
            {
                n[nc]=1 ;
                nc++;
            }
        }
        

        temp  = min(count[20] , count[8] , count[18]) ;
        if(temp>count[5])
            temp = count[5] ;
        if(temp>count[8])
            temp = count[8] ;
        
        if(temp>0  && count[5]>=2)
        {
            num=num+temp ;
            count[20]-=temp ;
            count[8]-=temp ;
            count[18]-=temp ;
            count[5]-=temp+1 ;   //
            for(j=0;j<temp;j++)
            {
                n[nc]=3 ;
                nc++;
            }
            
        }

        
        temp  = min(count[6] , count[9] , count[22]) ;
        if(temp>count[5])
            temp = count[5] ;
        if(temp>count[6])
            temp = count[6] ;

        if(temp>0)
        {
            num=num+temp ;
            count[6]-=temp ;
            count[9]-=temp ;
            count[22]-=temp ;
            count[5]-=temp ;
            for(j=0;j<temp;j++)
            {
                n[nc]=5 ;
                nc++;
            }
            
            
        }

        
        temp  = min(count[19] , count[22] , count[14]) ;
        if(temp>count[19])
            temp = count[19] ;
        if(temp>0  && count[5]>=2)
        {
            num=num+temp ;
            count[19]-=temp ;
            count[22]-=temp ;
            count[14]-=temp ;
            count[5]-=temp+1 ;   //
            for(j=0;j<temp;j++)
            {
                n[nc]=7 ;
                nc++;
            }
            
            
        }
        

        
        
        
        temp  = min(count[14] , count[9] , count[5]) ;
        if(temp>0 && count[14]>=2)
        {
            num=num+temp ;
            count[14]-=temp+1 ;   //
            count[9]-=temp ;
            count[5]-=temp ;
            for(j=0;j<temp;j++)
            {
                n[nc]=9 ;
                nc++;
            }

            
        }
        
        qsort (n, nc , sizeof(int), compare);
        printf("Case #%d: ",i+1);
        for(j=0;j<nc;j++)
        {
            cout<<n[j];
        }
        cout<<endl ;
      
        
        
    }
    return 0 ;
}