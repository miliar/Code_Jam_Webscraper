#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
int input(){
int t=0; char c;
c=getchar();
while(c<'0' || c>'9')
c=getchar();
while(c>='0' && c<='9')
{t=(t<<3)+(t<<1)+c-'0'; c=getchar();}
return t;
}
int checkpal(int n)
{
    int pal=0,i;
    int num=n;
    while(num!=0)
    {
        pal=pal*10+num%10;
        num=num/10;
    }
    if (n==pal)
        return 1;
    else return 0;
}
int main(){
freopen("C.in","r",stdin);
freopen("Cout.txt","w",stdout);
int sq,test,x,t,a,b,i,j,k,A,B;
double sqroot;
t=input();
for(test=1;test<=t;test++)
{
    int count=0;
    a=input();
    b=input();
    A=(int)(sqrt(a));
    if (A*A==a);
    else A++;
    B=(int)(sqrt(b));
    for(i=A;i<=B;i++)
    {
        sq=i*i;
        j=checkpal(i);
        if (j==0)
            continue;
        k=checkpal(sq);
        if (k==1)
            count++;
        //printf("%d ",sq );
    }
    printf("Case #%d: %d\n",test,count);
}

return 0;
}
