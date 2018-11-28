#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>

using namespace std;


double fun(double c,double f,double x,int num)
{
    double ret = 0;
    double v0 = 2;

    for(int i=0;i<num;i++)
    {
        ret += c/v0;
        v0 += f;
    }

    ret += x/v0;

    return ret;
}

int main()
{
    freopen("D:\\a.in","r", stdin);
    freopen("D:\\b.txt","w", stdout);

    int q;
    cin>>q;

    double c,f,x;

    for(int t=1;t<=q;t++)
    {
        cin>>c>>f>>x;

        double ans = x/2;
        int r = 0;
        if(x>c) r = x;
        int l = 0;

        while(l<=r)
        {
            //cout<<"lr:  "<<l<<" "<<r<<endl;
            int mid = (l+r)/2;
            int midmid = (l+mid)/2;

            double t1 = fun(c,f,x,midmid);
            double t2 = fun(c,f,x,mid);

            //cout<<midmid<<" "<<t1<<endl;
            //cout<<mid<<" "<<t2<<endl;

            ans = min(t1,ans);
            ans = min(t2,ans);

            if(t1<t2)
            {
                r=mid-1;
            }
            else
            {
                l =midmid+1;
            }
        }

        cout<<"Case #"<<t<<": ";
        printf("%.7f\n",ans);
    }

}
