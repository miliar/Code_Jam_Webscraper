#include <cstdio>


int main()
{
    int a[] = {1,4,9,121,484};
    int T, cases = 0;
    scanf("%d", &T);
    while(T--)
    {
        int A,B;
        scanf("%d%d",&A,&B);
        int count=0;
        for(int i =0;i<5;i++)
        {
            if(a[i]>=A && a[i]<=B)
            {
                count++;
            }
        }
        printf("Case #%d: %d\n", ++cases, count);
    }
    return 0;
}
