#include<bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    int cases =1;
    while(scanf("%d", &t)!=EOF)
    {
        while(t--)
        {
            printf("Case #%d: ", cases++);


        int a, b, c;

        scanf("%d %d %d", &a, &b, &c);

        for(int i=1; i<=a; i++)
        {
            if(i!=1)
            printf(" ");

            printf("%d", i);
        }

        printf("\n");
        }


    }
    return 0;
}
