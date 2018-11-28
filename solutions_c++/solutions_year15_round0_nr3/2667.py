
#include <iostream>
#include <cstdio>

#define I 2
#define J 3
#define K 4
using namespace std;

int multiplier[5][5];
int main()
{
    freopen("C-small.in","r",stdin);
    freopen("output.txt","w",stdout);
    for(int i=1;i<5;i++)
    {
        multiplier[1][i] = i;
    }
    {
    multiplier[2][1]=2;
    multiplier[2][2]=-1;
    multiplier[2][3]=4;
    multiplier[I][K]=-J;

    multiplier[J][1]=J;
    multiplier[J][I]=-K;
    multiplier[J][J]=-1;
    multiplier[J][K]=I;

    multiplier[K][1]=K;
    multiplier[K][I]=J;
    multiplier[K][J]=-I;
    multiplier[K][K]=-1;
    }
    int T;
    scanf("%d",&T);

    for(int it=1;it<=T;it++)
    {
        printf("Case #%d: ",it);
        int L,X;
        scanf("%d%d",&L,&X);
        int slen=L*X;
        string str;
        cin>>str;
        string s="";
        while(X--)
        {
            s+=str;
        }

        int sum=s[0]-'g';
        int index=1;
        int flag=0;

        while(sum!=I && index<slen)
        {
            if(sum<0)
            sum = -multiplier[-sum][s[index]-'g'];
            else
                sum = multiplier[sum][s[index]-'g'];

            index++;
        }

        if(sum==I && index<slen)
        {
            int sum2=s[index]-'g';
            index++;
            while(sum2!=J && index<slen)
            {
                if(sum2<0)
                sum2 = -multiplier[-sum2][s[index]-'g'];
                else
                    sum2 = multiplier[sum2][s[index]-'g'];

                index++;
            }
            if(sum2==J && index<slen)
            {
                int sum3=s[index]-'g';
                index++;
                while(index<slen)
                {
                    if(sum3<0)
                    sum3 = -multiplier[-sum3][s[index]-'g'];
                    else
                        sum3 = multiplier[sum3][s[index]-'g'];

                    index++;
                }
                if(sum3==K && index==slen)
                {
                    printf("YES\n");
                }
                else
                {
                    printf("NO\n");
                }

            }
            else
            {
                printf("NO\n");
            }

        }
        else
        {
            printf("NO\n");
        }
    }


}


