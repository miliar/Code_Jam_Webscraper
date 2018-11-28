#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int main()
{
    int T;cin>>T;
    for (int cases = 0; cases < T; ++cases)
    {
        double ans=0;
        double nows=2;
        double c,f,x;
        cin>>c>>f>>x;
        while(true)
        {   
            double tmp=c/nows;
            ans+=tmp;
            if((x-c)/nows < x/(nows+f)) 
            {
                ans+=(x-c)/nows;
                break;
            }
            nows+=f;
        }
        printf("Case #%d: ",cases+1);
        printf("%.7f\n",ans);
    }
    return 0;
}