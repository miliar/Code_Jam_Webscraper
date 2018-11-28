#include <iostream>
#include <cstdio>
#include <math.h>
#include <vector>
#include <string.h>
#include <algorithm>
#include <climits>
#include<fstream>
using namespace std;
int main()
{
    int i=0,j=0,t=0,c=1,a1=0,a2=0,c1=0,num=0;
	int arr1[4][4],arr2[4][4];
    scanf("%d",&t);
    while(t--)
    {
        int a[17]={0};
        c1=0;
        scanf("%d",&a1);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&arr1[i][j]);
                if(a1==(i+1))
                {
                    a[arr1[a1-1][j]]=1;
                }
            }
        }
        scanf("%d",&a2);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&arr2[i][j]);
                if(a2==(i+1))
                {
                    if(a[arr2[a2-1][j]]==1)
                    {
                        c1++;
                        num=arr2[a2-1][j];
                    }
                }
            }
        }
        if(c1==0)
        {
             printf("Case #%d: Volunteer cheated!\n",c);
        }
        if(c1==1)
        {
            printf("Case #%d: %d\n",c,num);
        }
        if(c1>1)
        {
             printf("Case #%d: Bad magician!\n",c);
        }
        c++;
    }
    return 0;
}
