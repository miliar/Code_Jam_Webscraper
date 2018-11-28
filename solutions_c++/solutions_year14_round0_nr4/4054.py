#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;
vector<double> N,K,a,b;
bool comp(double x,double y)
{
    return x>y;
}
int main()
{
    int x,y,t,i,j,k,n,ap,bp;
    double f;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        N.clear();
        K.clear();
        a.clear();
        b.clear();
        scanf("%d",&n);
        for(j=0;j<n;j++)
        {
            scanf("%lf",&f);
            N.push_back(f);
            a.push_back(f);
        }
        for(j=0;j<n;j++)
        {
            scanf("%lf",&f);
            K.push_back(f);
            b.push_back(f);
        }
        sort(N.begin(),N.end(),comp);
        sort(K.begin(),K.end(),comp);
        sort(a.begin(),a.end(),comp);
        sort(b.begin(),b.end(),comp);
        //printf("%lf\n",*(a.end()-1));
        j=x=0;
        ap=n-1;
        bp=0;
        //printf("%lf %lf\n",a[ap],b[ap]);
        while(!a.empty() && bp<n && a[0]<b[bp])
        {
            //ap--;
            a.pop_back();
            //printf("error");
            bp++;
            //printf("out");
        }
        /*while(ap>0 && bp<n && a[ap]<b[ap])
        {
            ap--;
            bp++;
        }*/
        while(!a.empty())
        {
            if(*(a.end()-1)>b[ap])
                {x++;
                ap--;}
            else
            {
                //ap--;
                bp--;
            }
            a.pop_back();
        }
        //x=n-bp;

        y=0;
        for(j=0;j<n;j++)
        {
            if(N[j]>K[0])
            {
                K.pop_back();
                y++;
                continue;
            }
            for(k=n-j-1;k>=0;k--)
            {
                if(N[j]<K[k])
                {
                    K.erase(K.begin()+k);
                    break;
                }
            }
        }
        printf("Case #%d: %d %d\n",i,x,y);
    }
    return 0;
}
