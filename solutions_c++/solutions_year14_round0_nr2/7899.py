#include<iostream>
#include<iomanip>
#include<cstdio>
using namespace std;
int main()
{
    freopen("ab.txt","r",stdin);
    freopen("cd.txt","w",stdout);
    int t,k=1;
    double c,f,x,s,cr,m,time;
    cin>>t;
    while(t-->0)
    {
        cr=2;
        cin>>c>>f>>x;
        s=0;
        time=x/cr;
        for(int i=1;;i++)
        {
            s=s+c/cr;
            cr=cr+f;
            if(s>time)
                break;
            m=x/cr+s;
            if(time>m)
                time=m;
        }
        cout <<"Case #"<<k<<": "<< std::fixed << std::setprecision(7)<<time<<"\n";
        k++;
    }
}
