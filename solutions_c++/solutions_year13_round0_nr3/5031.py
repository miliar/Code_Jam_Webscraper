#include<stdio.h>
#include<conio.h>
#include<math.h>
#include<stdlib.h>
int pal(int i )
{
int num ;
int dig , rev =0 ;
num = i ;
while(num>0)
{
dig = num % 10;
rev = rev * 10 + dig;
num = num / 10;
}
if (i == rev)
return 1 ;
else
return 0 ;

}

int main()
{
int t , n , i , j , a , b ,flag , flag2 , count , z=1  ;

FILE *f1,*f2 ;
f1 = fopen("input.txt","r");
f2 = fopen("output1.txt","w");
fscanf(f1,"%d",&t);
    while(t--)
    {
    fscanf(f1,"%d %d",&a,&b) ;
    count = 0 ;
    
        for( i=a ; i<=b ; i++)
        {
        n = (int)sqrt(i) ;
            if( n*n == i )
                if( pal(i) && pal(n))
                count++ ;
        }
    fprintf(f2,"Case #%d: %d\n",z,count);
    z++;
    }
fclose(f1);
fclose(f2);
getch();
return 0;
}
