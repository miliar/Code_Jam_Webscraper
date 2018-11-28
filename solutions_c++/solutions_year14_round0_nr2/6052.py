#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,temp = 1;
    cin>>t;
    while(t--)
    {
        double c,f,x,time,k,tm1,tm2;
        cin>>c>>f>>x;
        cout<<"Case #"<<temp++<<": ";
        k = 2;
        time = 0;
        while(1)
        {
            tm1 = x/k + time;
            tm2 = c/k + time + x/(f+k);
            if(tm1 <= tm2)
            {
                time = tm1;
                break;
            }
            else
            {
                time += c/k;
                k+=f;
            }
        }
        printf("%.7lf\n",time);
    }
    return 0;
}
