#include <stdio.h>
#include <set>

int main()
{
    int t;
    int n;
    scanf("%d",&t);
    for(int i = 0; i<t ; i++)
    {
        int counter = 1;
        scanf("%d", &n);
        if(n == 0)
            printf("Case #%d: INSOMNIA\n", i+1);
        else
        {


            std::set<int> s;
            while(s.size()<10)
            {
                int temp = n*counter;
                while(temp>0)
                {
                    s.insert(temp%10);
                    temp = temp/10;
                }
                counter++;
            }
            printf("Case #%d: %d\n", i+1, n*(counter-1));
        }


    }
    return 0;
}
