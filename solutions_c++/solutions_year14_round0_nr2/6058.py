#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
int main()
{
    //freopen("B-large (1).in", "r", stdin);
    //freopen("da.out", "w", stdout);
    int i, j, t;
    int cas = 1;
    double c, f, x, s, v;
    cin>>t;
    while(t--)
    {
        cin>>c>>f>>x;
        printf("Case #%d: ", cas++);
        double t1, t2, v;
        t1 = t2 = 0;
        v = 2.0;
        while(1){
            t2 = t1 + x/v;
            t1 = t1 + c/v;
            v += f;
            if(t2 <= t1 + x/v)break;
        }
        printf("%.7lf\n", t2);
    }
    return 0;
}
