#include <iostream>
#include <cstdio>
#include <set>

using namespace std;

int main()
{
    int t,r,f,w,u;
    scanf("%d", &t);
    
    for (int o=0; o<t; ++o)
    {
        scanf("%d %d", &r, &f);
        w=0;
        for (int i=r+1; ; i+=2)
        {
            u=i*i-(i-1)*(i-1);
            if (f>=u)
            {
                ++w;
                f-=u;
            }
            else break;
        }
        
        printf("Case #%d: %d\n", o+1, w);
    }



	return 0;
}