#include <cstdlib>
#include <cstdio>
#include <iostream>
#define cn 10000000
using namespace std;

bool check(int);
double c,f,x;
double box[10000050];

int main()
{

    freopen("B-large.in","r",stdin);
    freopen("cc","w",stdout);


    int t;
    int k=0;

    scanf("%d",&t);

    while(t--)
    {
        k++;
        scanf("%lf %lf %lf",&c,&f,&x);

        int low=0;
        int high=cn;

        box[0]=2;

        for(int i=1;i<=high;i++)
        {
            box[i]=box[i-1]+f;
        }

        while(low<high)
        {
            int mid=(low+high)/2;

            if(check(mid))
            {
                low=mid+1;
            }
            else
            {
                high=mid;
            }

        }

        double ans=0;

        for(int i=0;i<low;i++)
        {
            ans+= c/box[i];
        }

        ans+=x/box[low];

        printf("Case #%d: %.7lf\n",k,ans);

    }

}

bool check(int a)
{
    int b=a+1;

    if( x/box[a] > (c/box[a] + x/box[b]) )
        return true;
    else
        return false;

}
