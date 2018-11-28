#include <stdio.h>
#include <math.h>

int n[2],cnt=0,nmt;//notMoreThan
int num[2][55],ptVal=-1;
long long val[10100];
//FILE *fpW;

int isParlindrome(int ch)
{
    int i,j;
    for(i=0;i<n[ch];i++)
    {
        if(num[ch][i]!=num[ch][n[ch]-i-1])
            return 0;
    }
    return 1;
}

int isFair(long long value2)
{
    int i,j;
    int pt=-1;
    while(true)
    {
        num[1][++pt]=value2%10;
        value2/=10;
        n[1]=pt+1;
        if(value2<=0)
            break;
    }
    if(isParlindrome(1)==1)
        return 1;
    return 0;
}

int genNum(int pt)
{
    int i,j;
    if(pt==n[0])
    {

        /*for(int i=0;i<n[0];i++)
            printf("%d",num[0][i]);
        printf("\n");*/

        if(isParlindrome(0)==1)
        {
            int x=1;
            long long value=0,value2;
            for(i=0;i<n[0];i++)
            {
                value+=num[0][i]*x;
                x*=10;
            }
            value2=value*value;
            if(value2>nmt)
                return -1;
            if(isFair(value2)==1)
            {
                //cnt++;
                val[++ptVal]=value2;
                return 1;
            }
            return 0;
        }
        return 0;
    }
    for(i=0;i<10;i++)
    {
        if((i==0)&&(pt==0||pt==n[0]-1))
        {
            continue;
        }
        num[0][pt]=i;
        if(genNum(pt+1)==-1)
            return -1;
    }

}

int main()
{
    int i,j;
    int a,b,deciA,deciB,temp,file,nFile;
    double x;
    scanf("%d",&nFile);
    for(file=1;file<=nFile;file++)
    {

        scanf("%d %d",&a,&b);
        nmt=b;

        if(a<=0)
            a=0;
        if(b<=0)
            b=0;
        x=sqrt(a);      if(x>1)x--;         temp=(int)log10(x);    deciA=temp+1;
        x=sqrt(b)+1;    temp=(int)log10(x);    deciB=temp+1;

        //printf("deciA=%d deciB=%d\n",deciA,deciB);
        ptVal=-1;
        for(n[0]=1;n[0]<=deciB+1;n[0]++)
            genNum(0);

        //printf("%d\n",cnt);
        cnt=0;
        for(i=0;i<=ptVal;i++)
        {
            if(a<=val[i]&&val[i]<=b)
            {
                cnt++;
               // printf("%lld ",val[i]);
            }
        }
        printf("Case #%d: %d\n",file,cnt);

    }

    scanf(" ");
    return 0;
}
