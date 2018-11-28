#include <iostream>
#include <cstdio>

using namespace std;

int finish[10];

int counter = 0;

void process(unsigned long long int r)
{
    int a;
    while(r)
    {
        a = r%10;
        if(!finish[a])
        {
            counter++;
            finish[a] = 1;
        }
        r /= 10;

    }
}


int main()
{
    int i, t, n, j;
    unsigned long long int r;


    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);

    for(i = 0; i < 10; i++)
        finish[i] = 0;

    scanf("%d",&t);

    for(i = 0; i <t; i++)
    {
        scanf("%d",&n);

        if (!n)
        {
            printf("Case #%d: INSOMNIA\n",i+1);
            continue;
        }

        r = 0;
        counter = 0;
        for(j = 0; j < 10; j++)
            finish[j] = 0;


        while(counter != 10)
        {
            r += n;
            process(r);
            //printf("%llu\n",r);
        }

        printf("Case #%d: %llu\n",i+1,r);
    }



    return 0;
}
