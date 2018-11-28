#include<stdio.h>
#include<stdlib.h>
#include<string.h>
main()
{
    freopen("B-large.in","a+",stdin);
    freopen("output.txt","w+",stdout);
    int t;
    scanf("%d",&t);
    for(int k=1;k<=t;k++)
    {
        char A[105];
        scanf("%s",A);
        int Alen = strlen(A);
        printf("Case #%d: ",k);
        int stop = 0;
        int counter = 0;
        char temp=A[stop];
        //printf("%d",Alen);
        while(stop != Alen-1)
        {
            temp = A[stop];
            while(A[stop] ==A[stop+1] && stop!=Alen-1)
            {
                stop++;
            }
            if(stop == Alen-1)
                break;
            for(int i=0;i<=stop;i++)
            {
                A[i]=A[stop+1];
            }
            counter++;
            //printf("%d\n",stop);
        }
        if(temp=='-')
            printf("%d\n",counter+1);
        else
            printf("%d\n",counter);
    }
}
