#include<iostream>
#include<stdio.h>
using namespace std;

main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w+",stdout);
    double c,f,x,k,p,l,m,n,sp;
    int i,j;
    cout.setf(ios::fixed,ios::floatfield);
    //cout.precision(6);
    cin>>n;
    for(j=0; j<n; j++)
    {
        cin>>c>>f>>x;
        k=0;
        sp=2;
        while(1==1)
        {
            if(x/sp<=(c/sp)+(x/(sp+f))){k=k+x/sp; cout<<"Case #"<<j+1<<": "<<k<<endl; break;}
            else
            {
                    k=k+(c/sp);
                    sp=sp+f;
            }
            //cout<<k<<endl;
        }
    }
}
