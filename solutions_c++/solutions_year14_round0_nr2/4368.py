#include<iostream>
#include<cstdio>
#include<vector>
#include<set>

using namespace std;
#define For(a,b,c) for(a = b;a < c; a++)
#define rep(a,b) for(int a=0;a<b;a++)

int main()
{
    freopen ("B-large.in","r",stdin);
    freopen ("data.out","w",stdout);
    int t;
    double c,f,x,time,sumatime,respaux,resp;
    scanf("%d",&t);
    rep(T,t)
    {
        printf("Case #%d: ",T+1);
        cin>>c>>f>>x;
        sumatime = f;
        resp = x/2;
        time = c/2;
        f+=2;//por segundo
        respaux = time + x/f;
        while(respaux < resp)
        {
            resp = respaux;
            time += c/f;
            f+=sumatime;
            respaux = time + x/f;
        }
        printf("%.7lf\n",resp);
    }
}
