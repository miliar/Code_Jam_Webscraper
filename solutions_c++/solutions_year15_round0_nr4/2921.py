#include<stdio.h>
#include<iostream>
int main()
{
    int i,j,t,c,r,x;
    FILE *out;
    FILE *in;
   in=freopen("input.IN","r",stdin);
    out=freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
        scanf("%d%d%d",&x,&r,&c);
        if(x==1)
            printf("Case #%d: GABRIEL\n",i+1);
        else if(x==2 && (r*c)%2==0)
            printf("Case #%d: GABRIEL\n",i+1);
        else if(x==3 && ((r*c)%3==0 &&(r*c)>3))
                printf("Case #%d: GABRIEL\n",i+1);
        else if(x==4 && ((r*c)%4==0 && (r*c)>8))
            printf("Case #%d: GABRIEL\n",i+1);
        else if(x==5 && ((r*c)%5==0 && (r*c)>15))
                    printf("Case #%d: GABRIEL\n",i+1);
            else if(x==6 &&((r*c)%6==0 && (r*c)>24))
                printf("Case #%d: GABRIEL\n",i+1);
                else if(x==7 &&((r*c)%7==0 &&(r*c)>35))
                    printf("Case #%d: GABRIEL\n",i+1);
                else if(x==8 &&((r*c)%8==0&& (r*c)>48))
                    printf("Case #%d: GABRIEL\n",i+1);
                else if(x==9 &&((r*c)%9==0&& (r*c)>63))
                    printf("Case #%d: GABRIEL\n",i+1);
                else if(x==10 &&((r*c)%10==0&&(r*c)>80))
                    printf("Case #%d: GABRIEL\n",i+1);
                else if(x==11 && ((r*c)%11==0&&(r*c)>99))
                    printf("Case #%d: GABRIEL\n",i+1);
                else if(x==12 && ((r*c)%12==0&&(r*c)>120))
                    printf("Case #%d: GABRIEL\n",i+1);
                else if(x==13 &&((r*c)%13==0&&(r*c)>143))
                    printf("Case #%d: GABRIEL\n",i+1);
                else if(x==14&&((r*c)%14==0&&(r*c)>168))
                    printf("Case #%d: GABRIEL\n",i+1);
                else if(x==15&&((r*c)%15==0&&(r*c)>195))
                    printf("Case #%d: GABRIEL\n",i+1);
                else if(x==16&&((r*c)%16==0&&(r*c)>224))
                    printf("Case #%d: GABRIEL\n",i+1);
                else if(x==17&&((r*c)%17==0&&(r*c)>255))
                    printf("Case #%d: GABRIEL\n",i+1);
                else if(x==18&&((r*c)%18==0&&(r*c)>288))
                    printf("Case #%d: GABRIEL\n",i+1);
                else if(x==19&&((r*c)%19==0&&(r*c)>323))
                    printf("Case #%d: GABRIEL\n",i+1);
                else if(x==20&&((r*c)%20==0&&(r*c)>360))
                    printf("Case #%d: GABRIEL\n",i+1);
                else
                    printf("Case #%d: RICHARD\n",i+1);
    }
}
