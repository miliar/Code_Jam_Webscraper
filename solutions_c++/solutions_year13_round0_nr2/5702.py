#include<stdio.h>
#include<conio.h>

int calc(int a[10][10] , int x , int y )
{
int i , j ,count1 , count2 ,m , n ;
    for( i=0 ; i<x ; i++)
    {
        for( j=0 ; j<y ; j++)
        {
        count1=0;
        count2=0;
        
            if(a[i][j] == 1)
            {
                for( m = 0 ; m<y ; m++)
                {
                    if(a[i][m] == 2)
                    count1++;
                  
                }
                for( m = 0 ; m<x ; m++)
                {
                    if(a[m][j] == 2)
                    count2++;
                  
                }                    
                    
                if(count1 >0  && count2>0 )
                return 0;
            }
        }    
    }
return 1;
}

int main()
{

int t ,x , y, i , j ,w=1;
int a[10][10] ;
int ans ;

FILE *f1 , *f2 ;
f1 = fopen("ques2try.txt","r");
f2 = fopen("outputques2.txt","w");
fscanf(f1,"%d",&t);
while(t--)
{
fscanf(f1,"%d %d",&x,&y);
for(i=0 ; i<x ; i++)
{
for(j=0 ; j<y ; j++)
{
fscanf(f1,"%d",&a[i][j]);
}
}

ans = calc(a,x,y);
if(ans)
fprintf(f2,"Case #%d: YES",w);
else
fprintf(f2,"Case #%d: NO",w);
if(t>0)
fprintf(f2,"\n");
w++;
}

fclose(f1);
fclose(f2);
getch();
return 0;
}
