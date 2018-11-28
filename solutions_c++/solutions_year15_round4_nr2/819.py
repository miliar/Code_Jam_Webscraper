#include<fstream>
#include<iostream>
#include<stdio.h>;
using namespace std;
ifstream fin ("temp.in");
//ofstream cout ("temp.out");
int main ()
{
    freopen ("temp.out","w",stdout);
    int t;
    fin>>t;
    for (int i=1;i<=t;i++)
    {
        printf ("Case #%d: ",i);
        int n;
        double v,x;
        fin>>n>>v>>x;
        //if (i==15) cout<<n<<" "<<v<<" "<<x<<endl;
        double r1=0,r2=0,r3=0;
        double s1=0,s2=0,s3=0;
        for (int j=0;j<n;j++)
        {
            double r,c;
            fin>>r>>c;
            //if (i==15) cout<<r<<" "<<c<<endl;
            if (c<x) {r1+=r;s1+=r*(c-x);}
            else if (c>x) {r3+=r;s3+=r*(c-x);}
            else {r2+=r;}
        }
        double ans;
        if ((r1>0&&r3==0&&r2==0)||(r1==0&&r3>0&&r2==0)) printf ("IMPOSSIBLE\n");
        else if (r1==0||r3==0) {ans=v/r2;printf ("%.7lf\n",ans);}
        else
        {
            double a=-s1/s3;
            //cout<<a<<endl;
            if (a>1) {ans=v/(r3*a+r1+r2*a)*a;}
            else {ans=v/(r3*a+r1+r2);}
            printf ("%.7lf\n",ans);
        }
    }
}
