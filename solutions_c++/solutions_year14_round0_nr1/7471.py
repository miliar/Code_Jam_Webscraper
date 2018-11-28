#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <string>
using namespace std;
int a1[5],a2[5];
int main()
{
    int T,cas=1;
    cin>>T;
    while(T--)
    {
        int k,tmp;
        cin>>k;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                if(k == i)
                {
                    cin>>a1[j];
                }
                else cin>>tmp;
            }
        }
        cin>>k;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                if(k == i)
                {
                    cin>>a2[j];
                }
                else cin>>tmp;
            }
        }
        int cnt=0,val=0;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                if(a1[i] == a2[j]) val=a1[i],cnt++;
            }
        }
        if(cnt == 0) printf("Case #%d: Volunteer cheated!\n",cas++);
        else if(cnt > 1)
            printf("Case #%d: Bad magician!\n",cas++);
        else
        {

            printf("Case #%d: %d\n",cas++,val);
        }
    }
    return 0;
}
