#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;

main()
{
    int t,k=0;
    double c,f,x,sml,res,rt,r;
    freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
    cin>>t;
    while(k<t)
    {
        cin>>c>>f>>x;
        sml=10000000;
        rt=0;
        r=2;
        while(1)
        {
            res=x/r+rt;
            rt+=c/r;
            r+=f;
            if(sml>res)
                sml=res;
            else
                break;
        }
        cout<<"Case #"<<k+1<<": ";
        printf("%.7f\n",sml);
        k++;
    }
}
