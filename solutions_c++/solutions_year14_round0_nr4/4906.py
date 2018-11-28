#include <stdio.h>
#include <algorithm>
using namespace std;
bool fn(float a,float b)
{
    return a<b;
}
int main()
{
        int n,i,t;
        int I,T;
        float a[1000],b[1000];

        scanf("%d",&T);
        for(I=1;I<=T;I++)
        {

            scanf("%d",&n);
            for(i=0;i<n;i++)
                scanf("%f",&a[i]);
            for(i=0;i<n;i++)
                scanf("%f",&b[i]);

            printf("Case #%d: ",I);
            sort(a,a+n,fn);
            sort(b,b+n,fn);
            int j =0 ,ans = 0;
            for(i=0;i<n;i++)
            {
                while(j<n)
                {
                    if(b[i]<a[j])
                    {
                            ans++;
                            j++;
                            break;
                    }
                    j++;
                }
            }
            printf("%d ",ans);
            ans = n;
            for(i=0;i<n;i++)
            {
                t=-1;
                for(j=0;j<n;j++)
                {

                    if(b[j] > a[i] && b[j] != -1)
                    {
                   //printf("%f beats %f\n",b[j],a[i]);
                         //t=j;
                        b[j] = -1;
                        ans--;
                        break;

                    }
                }/*
                if(t != -1)
                {
                    printf("%f beats %f\n",b[t],b[i]);
                    b[t] = -1;
                    ans++;
                }*/
            }
            printf("%d\n",ans);
        }
        return 0;

}
