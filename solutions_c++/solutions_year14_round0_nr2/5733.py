#include <iostream>
#include <cstdio>

using namespace std;

double tempo (int n, double c, double f, double x)
    {double r=0;
    int i;

    for (i=0; i<n; i++)
        r += c/(2+i*f);
    r+= x/(2+n*f);

    return r;}


main()
    {int t, i, j, k;
    double c, f, x, ans;

    cin >>t;

    for(i=0; i<t; i++)
        {cin >> c >> f >> x;

        j=0;
        while (tempo(j, c, f, x) >= tempo(j+1, c, f, x))
            j++;

    ans = tempo(j, c, f, x);

    printf("Case #%d: %.7lf\n", i+1, ans);}

    return 0;}
