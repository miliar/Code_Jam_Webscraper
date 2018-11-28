#include<stdio.h>
#include<algorithm>

using namespace std;
bool mf (float i,float j) { return (i<j);}
int main()
{
    long int T,n,x,y,i,j,k,flag,ans1,ans2,arr[20],u,v;
    scanf("%ld",&T);
    double r,c,t,a1[1010],a2[1010];
for(k=1;k<=T;k++)
    {   flag=0;
    ans1=0;
    ans2=0;
        scanf("%ld",&n);
        for(i=0;i<n;i++)
        {
            scanf("%lf",&a1[i]);

        }
        sort(a1,a1+n,mf);
        for(i=0;i<n;i++)
        scanf("%lf",&a2[i]);

        sort(a2,a2+n,mf);
//         for(i=0;i<n;i++)
//        printf("%lf\n",a2[i]);

        x=0;
        y=0;
        u=n-1;
        v=0;
        j=0;
        while(j<n&&y<=u)
        {
            j++;
            // printf("haha %lf  %lf\n",a1[x],a2[y]);


            if(a1[x]>a2[y])
            {
            ans1++;
            x++;
            y++;




            }
            else
            {u--;x++;}

        }
        //ans1=ans1+n-j;
        j=0;
        u=0;
        while(j<n)
        {
            if(a1[u]>a2[j])
           {

            ans2++;//printf("%lf  %lf\n",a1[u],a2[j]);
           }
           else
           u++;
            j++;

        }

printf("Case #%ld: %ld %ld\n",k,ans1,ans2);
    }
}
