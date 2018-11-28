#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
#include<cmath>
using namespace std;
int main()
{
    freopen("B2.in","r",stdin);
    freopen("B2.out","w",stdout);
    int T;
    cin>>T;
    for(int cas = 1; cas <= T; cas++){
        cout<<"Case #"<<cas<<": ";
        double c,f,x, ans, fcost = 0;
        cin>>c>>f>>x;
        ans = x/2;
        for (int i = 1; i <= (int)(x/c); i++){
            fcost = fcost+ c/(f*(i-1)+2.0);
            double t = fcost+x/(f*i+2.0);
            if (ans > t) ans = t;
        }
        printf("%.7lf\n",ans);
    }
    return 0;
}


