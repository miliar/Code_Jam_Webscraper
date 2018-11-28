#include<cstdio>
using namespace std;

int main()
{
    int T,val,Smax,no,sum;
    scanf("%d",&T);
    char *S;
    for(int j=1;j<=T;j++)
    {
        scanf("%d",&Smax);
        S = new char[Smax+2];
        scanf("%s",S);
        sum = S[0]-48;no=0;
        for(int i=1;i<=Smax;i++)
        {
            val = S[i]-48;
            if(sum < i && val!=0)
                {
                    no += i-sum;
                    sum +=i-sum;
                }
            sum += val;
        }
        if(j!=T)
            printf("Case #%d: %d\n",j,no );
        else
            printf("Case #%d: %d",j,no);
        delete []S;
    }
    return 0;
}
