#include <iostream>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

int M[1000];
int main()
{

    freopen("F:\\input.txt","rb",stdin);
    freopen("F:\\output.txt","wb",stdout);
    int T,N;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        scanf("%d",&N);
        for(int j=0;j<N;j++)
        {
            scanf("%d",&M[j]);
        }
        int totalEaten =0;

        //method1
        for(int j=1;j<N;j++)
        {
            if(M[j] < M[j-1])
            {
                totalEaten += (M[j-1]-M[j]);
            }
        }
        printf("Case #%d: %d ",i,totalEaten);

        totalEaten = 0;
        int gmin = 100000000;
        bool isValid;
        bool isCalc = false;
        for(int j=1;j<N;j++)
        {
            if(M[j] < M[j-1])
            {
                int mushPerInterval = M[j-1] - M[j];
                totalEaten = 0;
                isValid = true;
                for(int k=1;k<N;k++)
                {
                    if(( M[k-1] - M[k] ) > mushPerInterval)
                    {

                        isValid = false;
                        break;
                    }
                    if((M[k-1])< mushPerInterval)
                    {
                        totalEaten += (M[k-1]);
                    }
                    else
                    {
                        totalEaten += mushPerInterval;
                    }
                }
                if(isValid)
                {
                    //printf(":%d:",mushPerInterval);
                    isCalc = true;
                    gmin = gmin < totalEaten ? gmin : totalEaten;
                }
            }
        }
        if(isCalc)
            printf("%d\n",gmin);
        else
            printf("0\n",gmin);

    }
    return 0;
}
