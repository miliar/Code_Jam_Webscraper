#include<cstdio>
#include<algorithm>
using namespace std;
float x[1005];
float y[1005];
int main()
{
    int a,b=0,c,d,i,count1,count2,j,k,l;
    scanf("%d",&a);
    while(b<a)
    {
        count1=0;
        count2=0;
        j=0;
        k=0;
        scanf("%d",&c);
       // float x[c],y[c];
        for(i=0;i<c;i++)
            scanf("%f",&x[i]);
        for(i=0;i<c;i++)
            scanf("%f",&y[i]);
        sort(x,x+c);
        reverse(x,x+c);
        sort(y,y+c);
        reverse(y,y+c);
        l=c-1;
        while(j<=l)
        {
            if(x[j]>y[k])
            {
                count1++;
                k++;
                j++;
            }
            else if(x[j]<y[k])
            {
                l--;
                k++;
            }
        }
        k=0;
        l=c-1;
        j=0;
        count2=0;
        while(j<=l)
        {
            if(x[k]>y[j])
            {
                count2++;

                k++;

                l--;
            }
            else if(x[k]<y[j])
            {
                j++;
                                k++;

            }
        }
        printf("Case #%d: %d %d\n",b+1,count1,count2);


        b++;
    }
    return 0;
}
