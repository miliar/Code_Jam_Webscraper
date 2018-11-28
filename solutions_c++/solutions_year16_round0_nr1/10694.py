#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.txt", "r" ,stdin);
    freopen("sabbiroutput.txt", "w" ,stdout);

    long long int a,b,c,i,j,k=0;

    map<long long int ,long long int >ma;
    scanf("%lld",&a);

    for(i=1; i<=a; i++)
    {
        scanf("%lld",&b);
        ma.clear();k=0;
        if(b==0)printf("Case #%lld: INSOMNIA\n",i);
        else
        {
            j=b;
            while(j)
            {

                if(ma.size()==10)
                {
                    printf("Case #%lld: %lld\n",i,j-b);
                    break;
                }
                else if(j<10)
                {
                    ma[j]++;
                }
                else if(j>9)
                {

                    c=j;
                    while(c)
                    {
                        ma[c%10]++;
                        c/=10;
                    }
                }
                j+=b;
            }

        }
    }
}
