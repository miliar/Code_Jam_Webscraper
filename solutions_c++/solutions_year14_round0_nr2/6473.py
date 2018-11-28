#include<cstdio>
#include<iostream>
using namespace std;
int main()
{
    int cas=0,t,count,ans,i,j;
    long double c,f,x,lc,lf,lx,a,la,ft,rate;
    freopen("B-small-attempt0.in","r",stdin);
    freopen("b-output.txt","w",stdout);
    cin>>t;
    while(cas++<t){
        cin>>c>> f >> x ;
        ft = 0;
        rate = 2.0;
        a = x/rate;
        do{
            la = a;
            ft += c / rate;
            rate += f;
            a = ft + (x/rate);
        //cout<<"Case #"<<cas<<": "<<fixed<<a<<"\n";
        }while(la>a);
        cout.precision(7);
        cout<<"Case #"<<cas<<": "<<fixed<<la<<"\n";

            //printf("Case #%d: Volunteer cheated!\n",cas);
    }
    return 0;
}
