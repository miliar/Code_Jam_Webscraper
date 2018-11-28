#include <bits/stdc++.h>

using namespace std;
int N=16;
int dig[16];
int leftO=50;
void fillDig(int idx)
{
    if(leftO==0)return;
    if(idx==N-1)
    {
        bool ok=true;
        vector<int> out;
        long long num;
        for(int base=2;base<=10;base++)
        {
            long long number=0,pw=1;
            for(int i=N-1;i>=0;i--)
            {
                if(dig[i])number+=pw;
                pw*=base;
            }
            bool found=false;
            long long div;
            long long sqr=sqrt(number);
            for(int i=2;i<=sqr;i++)
            {
                if(number%i==0)
                {
                    div=i;
                    found=true;
                }
            }
            if(!found)return;
            num=number;
            out.push_back(div);
        }
        if(ok)
        {
            printf("%lld ",num);
            for(int i=0;i<out.size();i++)
                printf("%d ",out[i]);
            printf("\n");
            leftO--;
        }
        return;
    }
    dig[idx]=0;
    fillDig(idx+1);
    dig[idx]=1;
    fillDig(idx+1);
}
int main()
{
    freopen("out.out","w",stdout);
    dig[0]=1;
    dig[N-1]=1;
    printf("Case #1:\n");
    fillDig(1);

    return 0;
}
