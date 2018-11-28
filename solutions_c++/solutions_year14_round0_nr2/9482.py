#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
    int T;
    scanf("%d",&T);
    float C,F,X;
    for(int i=1;i<=T;i++)
    {
        scanf("%f",&C);
        scanf("%f",&F);
        scanf("%f",&X);
        float ans=X/2.00;
        for(int j=2; ;j++)
        {
            float temp = X/float(2+(j-1)*F);
            for(int k=1;k<j;k++)
            {
                temp+=C/float(2+(k-1)*F);
            }
            if(temp<ans) ans=temp;
            else break;
        }
        printf("Case #%d: %.7f\n",i,ans);
  }
    return 0;
}

