#include<iostream>
#include<stdio.h>
#define intin(a) scanf("%d",&a)
using namespace std;
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("Coutput.txt","w",stdout);
    int i,x=0,cases,a,b,m[2000]={0};
    for(i=1;i<1001;i++)
    {   if(i==1||i==4||i==9||i==121||i==484) m[i]=m[i-1]+1;
        else m[i]=m[i-1];
    }
    intin(cases);
    while(++x<=cases)
    {
        intin(a);intin(b);
        //if(b==a && (b==1||b==4||b==9||b==121||b==484))printf("Case #%d: 1\n",x);

        if(b==1||b==4||b==9||b==121||b==484){
            if(a==1||a==4||a==9||a==121||a==484)
                printf("Case #%d: %d\n",x,m[b]-m[a]+1);
            else
                printf("Case #%d: %d\n",x,m[b]-m[a]);}

        else{
            if(a==1||a==4||a==9||a==121||a==484)
                printf("Case #%d: %d\n",x,m[b]-m[a]+1);
            else
                printf("Case #%d: %d\n",x,m[b]-m[a]);}
    }
}
