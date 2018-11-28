#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;
typedef long double Double;

int t;
int n;
Double V,X;
pair<Double,Double> Tubes[111]; ///first - temp, second - speed
const Double EPS=0.000000000001;
const Double EPS_SMALLER=0.00000001;

int state;

Double total_temp,total_power;

Double FABS(Double a)
{
    if (a<0.0)
    return -a;
    else
    return a;
}

bool Equal(Double a,Double b)
{
    return FABS(a-b)<EPS;
}

bool Check(Double k)
{
    Double TotalVolume=0.0;
    int i;
    Double add_pow;
    bool nicely;

    for (i=1;i<=n;i++)
    {
        TotalVolume+=k*Tubes[i].second;
    }

    if (TotalVolume<V && !Equal(TotalVolume,V))
    return false;

    if (state==0)
    return true;
    else if (state==1)
    {
        total_temp=0.0;
        total_power=0.0;

        nicely=false;
        for (i=n;i>=1;i--)
        {
            if (Tubes[i].second*k < V-total_power*k)
            {
                add_pow=Tubes[i].second;
            }
            else
            {
                add_pow=(V-total_power*k)/k;
                nicely=true;
            }

            total_temp=(add_pow*Tubes[i].first+total_temp*total_power)/(add_pow+total_power);
            total_power+=add_pow;

            if (nicely)
            {
                if (total_temp>X || Equal(total_temp,X))
                return true;
            }
        }

        if (Equal(total_power*k,V))
        {
            if (total_temp>X || Equal(total_temp,X))
            return true;
        }

        return false;
    }
    else
    {
        total_temp=0.0;
        total_power=0.0;

        nicely=false;
        for (i=1;i<=n;i++)
        {
            if (Tubes[i].second*k < V-total_power*k)
            {
                add_pow=Tubes[i].second;
            }
            else
            {
                add_pow=(V-total_power*k)/k;
                nicely=true;
            }

            total_temp=(add_pow*Tubes[i].first+total_temp*total_power)/(add_pow+total_power);
            total_power+=add_pow;

            if (nicely)
            {
                if (total_temp<X || Equal(total_temp,X))
                return true;
            }
        }

        if (Equal(total_power*k,V))
        {
            if (total_temp<X || Equal(total_temp,X))
            return true;
        }

        return false;
    }
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large-output.txt","w",stdout);

    int i;
    int test;
    Double l,r,mid;
    Double best;

    scanf("%d",&t);

    for (test=1;test<=t;test++)
    {
        scanf("%d",&n);
        cin>>V>>X;

        for (i=1;i<=n;i++)
        {
            cin>>Tubes[i].second>>Tubes[i].first;
        }

        sort(Tubes+1,Tubes+1+n);

        total_temp=0.0;
        total_power=0.0;
        for (i=1;i<=n;i++)
        {
            total_temp=(total_temp*total_power+Tubes[i].first*Tubes[i].second)/(total_power+Tubes[i].second);
            total_power+=Tubes[i].second;
        }

        if (Equal(total_temp,X))
        state=0;
        else if (total_temp<X)
        state=1;
        else
        state=2;

        l=0.0000001;
        r=100000000.0;
        best=-1.0;

        while(r-l>EPS_SMALLER)
        {
            mid=(l+r)/2.0;

            if (Check(mid))
            {
                r=mid;
                best=mid;
            }
            else
            l=mid;
        }

        printf("Case #%d: ",test);

        if (best<0.0)
        printf("IMPOSSIBLE\n");
        else
        printf("%.8f\n",(double)best);
    }
}
