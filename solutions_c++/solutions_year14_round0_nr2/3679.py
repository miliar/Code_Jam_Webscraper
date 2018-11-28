#include <iostream>
#include <cstdio>

using namespace std;


double c, f, x, minn, time, v, q;
int t;

int main()

{
    freopen("input.txt","r", stdin);
    freopen("output.txt","w", stdout);
    cin>>t;
    for (int tt = 0; tt < t; tt++)
    {
        time = 0;
        v = 2;
        minn = 100000000000;
        scanf("%lf%lf%lf", &c, &f, &x);
        while (true)
        {
            q = time + x / v;
            if (q < minn) minn = q;
                else break;
            time += c/v;
            v+=f;
        }
        cout<<"Case #"<<tt+1<<": ";
        printf("%lf\n",minn);
    }
}

