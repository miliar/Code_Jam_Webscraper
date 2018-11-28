#include<cstdio>
#include<iostream>
#include<string.h>
using namespace std;
int main()
{
	int t;
	freopen("A-large.in", "r", stdin);
	freopen("A-largeOUT.txt", "w", stdout);
	scanf("%d\n",&t);
	int y = t;
	while( t--)
	{
           char str[101];
           int n=0;
           char orig[101];
           int res=0;
           char x;
           int ee=0;
           int pp[100]={0};
          // gets(str);
          int g;
          scanf("%s %d\n",str,&n);
          
           //printf(" string is %s \n",str);
         //  printf(" value of n is : %d  \n",n);
      
           int length =strlen(str) ;
              // printf(" length is %d \n",length);
           for( int i=0; i<=length-n ; i++ )
           {     int count =0;
                for(int j=i;  j< i+n; j++ )
                 {
                         if( str[j] != 'a' && str[j]!= 'e' && str[j]!='i' && str[j]!='o' && str[j]!= 'u')
                    count++;  
                    else break;
                 }
                 if( count < n) 
                 continue;
                 else
                 { //printf(" position %d has consecutive consonant \n", i);
                   pp[i]=1;  }
                   //printf(" incresed res by %d-%d-%d+1  = %d ", length,n,i, (length-n-i+1) );  
           }   
           for(int u=0 ; u<=length-n; u++ )
            for( int f=u; f<length; f++) 
             {  if( pp[f] == 1 )
                 {//printf( " adding %d-%d-%d+1 \n", length,f,n,1);
               res+=length-f-n+1;    break;}
               }     
       printf("Case #%d: %d\n", y-t , res);
       }
}              
               
