#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    int t,i;
    double c,f,x,ans,tme,prsnt,speed;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        ans=0.0;
        speed=2;
        //tme=0.0;
        //prsnt=0.0;
        cin>>c>>f>>x;
        while(ans+x/speed > (ans+c/speed+x/(speed+f)))
        {
            ans = ans+(c/speed);
            speed = speed+f;
            //cout<<"ans="<<ans<<endl;

        }
        ans+=x/speed;
        cout<<"Case #"<<i<<": ";
        //cout<<ans+(x-prsnt)/speed<<endl;
        printf("%0.7f\n",ans);
    }
    return 0;
}
