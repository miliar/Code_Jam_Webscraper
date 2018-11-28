#include<fstream>
#include<iostream>
#include<cstdlib>
#include<cstdio>
using namespace std;
int main()
{
    //freopen("in.txt","r",stdin);
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int ctr=1,T;
    double C,F,X,R,RF,ans,CT,LT;
    cin>>T;
    while(ctr<=T)
    {
        cin>>C>>F>>X;
        RF=(F*X)/C;
        R=2.0;
        CT=0.0;
        LT=X/R;
        ans=CT+LT;
        //printf("RF: %.7lf\n",RF);
        while(R+F<=RF)
        {
            CT+=C/R;
            LT=X/(R+F);
            ans=CT+LT;
            //printf("%.7lf\n",ans);
            R+=F;
            //cout<<"R: "<<R<<endl;
        }
        cout<<"Case #"<<ctr<<": ";
        printf("%.7lf\n",ans);
        ctr++;
    }
}
