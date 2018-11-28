#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int tc;
    double c,f,x,_x,mn,tmp,r;

    scanf("%d",&tc);
    for(int t=1; t<=tc; t++)
    {
        scanf("%lf%lf%lf",&c,&f,&x);

        int i=0;
        _x = 0;
        mn = 100000;
        while(true)
        {
            r=i*f+2.0;
            tmp = _x + x/r;
            if(mn>tmp) mn = tmp;
            else break;
            _x += c/r;
            i++;
        }
        printf("Case #%d: %lf\n",t,mn);
    }
}
