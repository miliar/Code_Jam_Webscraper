#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#define Mx 1111

int main()
{
    //freopen("Bin.txt","r",stdin);
    //freopen("Bout.txt","w",stdout);
    int i,T,t,k=1;
    char Qa[Mx],Sa[Mx],A[Mx];
    char Qb[Mx],Sb[Mx],B[Mx];
    long a,b,r,y,x;
    scanf("%d",&T);
    getchar();

    while(T--)
    {
        scanf("%d %d",&a,&b);
        r=0;
        y =(int) (ceil(sqrt(a)));
        x = sqrt(b);
        for(i=y; i<=x; i++)
        {
            t=i;
            itoa(t, A, 10);
            itoa(t*t, B, 10);
            strcpy(Qa,A);
            strcpy(Qb,B);

            strcpy(Sa,A);
            strcpy(Sb,B);

            strrev(Qa);
            strrev(Qb);

            if((!strcmp(Qa,Sa)) && (!strcmp(Qb,Sb)))
            {
                r++;
            }
        }
        printf("Case #%d: %d\n",k++,r);
    }

    return 0;
}

