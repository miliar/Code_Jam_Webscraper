#include <iostream>
#include <cstdio>
#include <limits.h>
#include <string.h>
#include <algorithm>

using namespace std;



int main()
{
    freopen("myfile.txt","r",stdin);
    freopen("myfile2.txt","w",stdout);
    int test,numb=1;
    scanf("%d",&test);
    while(test>=numb)
    {
        int x,y,k;
        scanf("%d%d%d",&x,&y,&k);
        int counter=0;
        for(int i =0 ; i < x ; i++)
        {
            for(int j= 0; j<y ;j++)
            {
                int t=i&j;
                if(t<k)
                    {
                        counter++;
                    }
            }
        }

        printf("Case #%d: %d\n",numb,counter);
        numb++;
    }
}
