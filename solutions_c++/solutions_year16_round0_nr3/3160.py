#include <iostream>
#include <cmath>
using namespace std;

int IsPrime(int number)
{
    int i;
    for (i=2; i*i<=number; i++)
    {
        if (number % i == 0)
            return 0;
    }
    return 1;
}

void generator(int  *arr , int m , int n  )
{
    
    int dec=m  , i=0 ;
    while(dec>0)
    {
        *(arr+i ) =dec%2 ;
        i++;
        dec=dec/2 ;
    }
    while(i<n)
    {
        *(arr+i)=0;
        i++;
    }
}

int calc(int *arr1 , int base  , int n )
{
    int i , sum=0 ;
    for(i=0;i<n;i++)
    {
        sum+=(*(arr1 + n-1-i) )*pow(base,i) ;
    }
    return sum ;
}

void printkar( int *arr2 , int n , int *arr3  )
{
    int temp , j , k   ;
    for(j=2;j<=10;j++)
    {
        temp=*(arr3 + j ) ;
        for(k=2 ;k<temp ;k++)
        {
            if(temp%k==0)
                break;
        }
        printf("%d ",k);
        
    }
}



int main()
{
    int t, i ;
    cin>>t;
    for(i=0;i<t;i++)
    {
        int n , j ;
        cin>>n>>j;
        int a[n] ;
        int b[11] ;
        b[0]=0 ; b[1]=0 ;
        int count=0 , k , l , temp , m , flag=0 ;
        printf("Case #%d:\n",i+1);
        for(k=0;k<pow(2,n);k++)
        {
            
            generator (a, k , n ) ;
            
            if(a[0]==1 && a[n-1]==1)
            {
                
                flag=0;
                
                for(l=2;l<=10;l++)
                {
                    
                    temp=calc( a , l , n );
                    b[l]=temp ;
                    if( IsPrime(temp) )
                    {
                        flag=1;
                        break;
                        
                    }
                }
                
          
                if(flag==0)
                {
                    
                    count++ ;
                    for(m=0;m<n;m++)
                        cout<<a[m];
                    
                    cout<<" ";
                    
                    printkar(a,n,b);
                    cout<<endl ;
                }
                
            }
            if(count==j)
                break;
        } // end of k
    } // end of i
    
    
    return 0;
}