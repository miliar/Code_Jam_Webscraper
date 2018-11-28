#include <iostream>
#include <cstdio>

using namespace std;

int t;
double curr, d[100005], c, f, x;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%i", &t);
    for(int ti=0; ti<t; ti++)
    {
        int i;
        cin >> c >> f >> x;
        d[0]=x/(double)2;
        for(i=1; i<100005; i++)
        {
            d[i]=d[i-1]+(c-x)/(2.0+(double)(i-1.0)*f)+x/(2.0+(double)i*f);
            if(d[i]>d[i-1])
            {
                printf("Case #%i: %.7f\n", ti+1, d[i-1]);
                break;
            }
        }
    }
    return 0;
}
