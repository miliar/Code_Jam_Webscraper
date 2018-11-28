#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int cas=1;cas<=t;cas++)
    {
        printf("Case #%d: ",cas);
        double c,f,x;
        cin>>c>>f>>x;
        double tot=0,ans=x/2.;
        //double sum=0;
        for(int i=1;i<100000;i++)
        {
            double temp=c/(2+(i-1)*f);
           // sum+=temp*(2+(i-1)*f)-c;
            tot+=temp;
            //cout<<temp<<endl;
            //printf("%.7lf\n",x/(2+i*f));
            //cout<<x/(2+i*f)<<endl;
            ans=min(ans,tot+x/(2+i*f));
            //printf("%.6lf\n",ans);
        }
        printf("%.7lf\n",ans);
    }
}
