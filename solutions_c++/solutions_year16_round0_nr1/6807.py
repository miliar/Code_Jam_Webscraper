#include <bits/stdc++.h>

using namespace std;

long long int flag = 0;


void setBit(int n)
{

    flag |= (1 << n);
}

bool isOkay()
{
    //printf("%lld\n", flag);
    if(flag == 1023)
    {

        return true;
    }
    else
    {

        return false;
    }
}



bool check(long long int n)
{
    while(n != 0)
    {
        int dig = n % 10;
        setBit(dig);
        n /= 10;
    }

    return isOkay();

}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    long long int n = 0;
    int tc = 0;
    scanf("%d", &tc);
    int cs = 1;

    while(tc--)
    {
        scanf("%lld", &n);
        if(n == 0)
        {
            printf("Case #%d: INSOMNIA\n", cs++);

        }
        else
        {
            int mult = 1;
            long long int temp = n;
            while(!check(temp))
            {
                mult++;
                temp = mult * n;
            }
            printf("Case #%d: %lld\n", cs++, temp);
        }

        flag = 0;
    }
    return 0;
}
