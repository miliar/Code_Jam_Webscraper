#include<stdio.h>
int getmax(int *p,int N)
{
    int i;
    int pos,max;
    max=-1;
    for(i=0;i<N;i++)
    {
        if(max<p[i])
        {
            max=p[i];
            pos=i;
        }
    }
    return pos;
}
bool check(int *p,int N,int total,int index)
{
    int i;
    for(i=0;i<N;i++)
    {
        if(i!=index)
        {
            if(p[i]>((total-1)/2))
            {
                return false;
            }
        }
        else
        {
            if((p[i]-1)>((total-1)/2))
            {
                return false;
            }
        }
    }
    return true;
}
int main()
{
    int T,N,S[30],i,j,total,index;
    scanf("%d", &T);
    for(i=0;i<T;i++)
    {
        total=0;
        scanf("%d", &N);
        for(j=0;j<N;j++)
        {
            scanf("%d", &S[j]);
            total+=S[j];
        }
        printf("Case #%d: ", i+1);
        while(total!=0)
        {
            index=getmax(S,N);
            printf("%c", index+65);
            S[index]--;
            total--;
            if(total==0)
                break;
            index=getmax(S,N);
            if(check(S,N,total,index))
            {
                printf("%c", index+65);
                S[index]--;

                total--;
            }
            printf(" ");
        }
        printf("\n");
    }
}
