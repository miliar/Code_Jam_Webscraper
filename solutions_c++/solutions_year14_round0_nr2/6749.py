
#include<iostream>
#include<cstdio>
using namespace std;
main()
{
    int t;
    double c, f, x;
    double ans, n1,n2,pre;
    scanf("%d",&t);
    int z = 0;
    while(++z <= t)
    {
        cin >> c >> f >> x ;
        int i = 0;
        ans = 0;
        pre = x/2;
        while(true)
        {
            n1 = pre;
            pre = x/((f*(i+1))+2);
            n2 = c/((f*i)+2);
            if(n1< pre+n2)
            {
                ans += n1;
                break;
            }
            ans += n2;
            i++;


        }
        printf("Case #%d: %.7lf\n",z,ans);
    }
    return 0;
}
