#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<map>
#include<set>

using namespace std;

int vet[2000];

int main()
{
    int t;
    int cases =1;


    scanf("%d", &t);

    while(t--)
    {

        int n;
        int y=0, z=0;
        int xpto;
        scanf("%d", &n);
        int last;
        scanf("%d", &last);
        vet[0] = last;
        int bigger = 0;

        for(int i=1; i<n; i++)
        {
            scanf("%d",&xpto);
            vet[i] = xpto;

            if(xpto<last)
            {
                y+= last - xpto;
                bigger = max(last - xpto,bigger);
            }

            last = xpto;
        }

        //printf("%d\n", bigger);

        for(int i=0; i<n-1; i++)
        {
            z+= vet[i] < bigger ? vet[i] : bigger;

        }

        printf("Case #%d: %d %d\n", cases++, y,z);
    }
}
