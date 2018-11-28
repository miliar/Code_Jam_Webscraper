#include <stdio.h>
#include <math.h>
long long int tempj=0;
int divisorList[9]; //NOTE: 2 to 10
int notPrime(long long int no)
{
    for(long long int i=2;i<=sqrt(no);i++)
    {
        if(no % i == 0)
            return i;
    }
    return -1; 
}

int jamcoin(int coin[],long long int n)
{
    /*printf("jamcoin called for:");
    for(long long int i=0;i<n;i++)
        printf("%d",coin[i]);
    printf("\n");*/
    for(int i=2;i<=10;i++)
    {
        long long int no=0;
        for(long long int j=0;j<n;j++)
            no += coin[n-j-1] * pow(i,j);
        //printf("no=%lli for i=%d\n",no,i);
        int divisor = notPrime(no);
        if(divisor == -1)
            return 0;
        else
        {
            divisorList[i-2] = divisor;
        }     
    }
    return 1;   
}

void permute(long long int n,long long int j,int coin[],int pos)
{
    if(pos == n-1) //number formed
    {
        if(tempj == j)
            return;
        int validity = jamcoin(coin,n);
        if(validity == 1)
        {
            //printf("base case\n");
            for(long long int i=0;i<n;i++)
                printf("%d",coin[i]);
            for(int i=0;i<9;i++)
                printf(" %d",divisorList[i]);
            printf("\n");
            tempj++;
            //printf("tempj updated to %lli\n",tempj);
        }
    }
    else
    {
        coin[pos] = 0; //during backtracking,it is important
        permute(n,j,coin,pos+1);
        coin[pos] = 1;
        permute(n,j,coin,pos+1);
    }    
}

int main()
{
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        long long int n,j;
        scanf("%lli%lli",&n,&j);
        printf("Case #%d:\n",t);
        tempj=0;
        int coin[n];
        coin[0] = coin[n-1] = 1;
        permute(n,j,coin,1);
    }
}