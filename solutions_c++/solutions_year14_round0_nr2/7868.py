#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;
double c,f,x;
int main()
{
    #ifndef ONLINE_JUDGE
        freopen("B-large.in","r" ,stdin);
         freopen("out.txt","w" ,stdout);
    #endif // ONLINE_JUDGE


    int T,cas=0;
    cin>>T;
    while(T--){
        scanf("%lf%lf%lf",&c,&f,&x);
        double time = 0.0,y=2.0;
        while(1)
        {
            if(time + x/y <= time + c/y + x/(y+f))
            {
                time += x/y;
                break;
            }
            else{
                time += c/y;
                y += f;
            }
        }
         printf("Case #%d: %.7f\n",++cas,time);
    }
    return 0;
}
