#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    int t,r,i,j,m;
    double c,f,x,rate,k,ans;
    freopen("B-large.in","r",stdin);
    freopen("bout.txt","w",stdout);
    cin>>t;
    r=1;
    while(t--)
    {
        cin>>c>>f>>x;
        m=(int)(x/c);
        k=0.000;
        ans=10000000000LL;
        rate=2.00000;
        while(k<ans)
        {
            //cout<<((x/rate)+k)<<endl;
            if(ans>((x/rate)+k))
            {
                ans=((x/rate)+k);
            }
            k+=(c/rate);
            rate+=f;
        }
        cout<<"Case #"<<r<<": ";
        r++;
        printf("%.7lf\n",ans);
    }


}
