#include <iostream>
#include <cstring>
#include <cstdio>
#include <fstream>
#define eps 0.0000000000001

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    double C,F,X;
    int T;
    cin>>T;
    double ans,ans1;
    for(int t=1;t<=T;t++)
    {
        scanf("%lf%lf%lf",&C,&F,&X);
        ans=1.0*X/2;
        ans1=1.0*C/2+1.0*X/(2+F);
        int i=1;
        while(ans+eps>ans1)
        {
            ans-=1.0*X/(2+(i-1)*F);
            ans+=1.0*C/(2+(i-1)*F)+1.0*X/(2+i*F);
            ans1=ans1-1.0*X/(2+i*F);
            ans1=ans1+1.0*C/(2+i*F)+1.0*X/(2+(i+1)*F);
            i++;
//            cerr<<ans<<" "<<ans1<<endl;
        }
        printf("Case #%d: %.8lf\n",t,ans);
    }
    return 0;
}
