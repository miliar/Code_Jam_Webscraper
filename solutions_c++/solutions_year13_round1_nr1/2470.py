#include<stdio.h>
#include<conio.h>

int main(){
int T,r,t,i,j;
scanf("%d",&T);
for(i=0;i<T;i++)
{
int flag=0,s=0,a;
scanf("%d",&r);
scanf("%d",&t);
while(s<=t){
            a=((r+1)*(r+1))-(r*r);
            s=s+a;
            flag++;
            r=r+2;
            }
            printf("Case #%d: %d\n",i+1,flag-1);
                 
}
getch();
return 0;
}
