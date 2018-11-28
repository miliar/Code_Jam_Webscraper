#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair
#define all(X) (X).begin(),(X).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

int N,i,j,T;
long double C,F,X,ans,cur;

int main()
{
    scanf("%d",&T);
    for(int t = 1; t <= T; t++)
    {
        scanf("%Lf %Lf %Lf",&C,&F,&X);
        ans = 0;
        cur = 2;
        while(X/cur > C/cur + X/(cur+F))
        {
            ans += C/cur;
            cur += F;
        }
        ans += X/cur;
        printf("Case #%d: %.10Lf\n",t,ans);
    }
    
    return 0;
}

