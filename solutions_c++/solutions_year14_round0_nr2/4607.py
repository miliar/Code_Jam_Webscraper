#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;

    for(int ti=0;ti<t;ti++)
    {
        cout<<"Case #"<<ti+1<<": ";

        double C,F,X;

        cin>>C>>F>>X;
        double ans=100000000;
        for(int i=0;i<=X;i++)
        {
            double tmp=0;

            for(int j=0;j<i;j++)
            {
                tmp+=C/(2+j*F);
            }
            tmp+=X/(2+i*F);

            ans=min(tmp,ans);
        }
        printf("%.7f\n",ans);
    }
    return 0;
}
