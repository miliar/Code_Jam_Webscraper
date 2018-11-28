#include <cstdio>
#include <algorithm>

using namespace std;

double s[111111];

int main()
{
    int T, t=1, i;
    double c, f, x, ans;
    scanf("%d", &T);
    while(T--)
    {
        scanf("%lf %lf %lf", &c, &f, &x);
        s[0]=0;
        ans=x/2;
        for(i=1; i<111111; i++)
        {
            s[i]=s[i-1]+1/(2+(i-1)*f);
            ans=min(ans, x/(2+i*f)+c*s[i]);
        }
        printf("Case #%d: %.7lf\n", t++, ans);
    }
    return 0;
}
