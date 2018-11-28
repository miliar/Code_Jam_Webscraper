#include <cstdio>
#include <algorithm>
#include <set>
#include <queue>
using namespace std;

int t[6];

int main ()
{
    int a,b,c,d,e,f,n,z;

    scanf ("%d", &z);

    for (a=1; a<=z; a++)
    {
        scanf ("%d", &n);

        for (b=0; b<n; b++)
            scanf ("%d", &t[b]);

        sort(t,t+n);

        if (t[n-1]<=3)
            printf ("Case #%d: %d\n", a, t[n-1]);
        else
        {
            if (t[n-1]==4)
            {
                if (n==1 || t[n-2]<=2)
                    printf ("Case #%d: %d\n", a, 3);
                else
                    printf ("Case #%d: %d\n", a, 4);
            }
            else
            {
                if (t[n-1]==5)
                {
                    if (n==1 || t[n-2]<=3)
                        printf ("Case #%d: %d\n", a, 4);
                    else
                        printf ("Case #%d: %d\n", a, 5);
                }
                else
                {
                    if (t[n-1]==6)
                    {
                        if (n==1 || t[n-2]<=3)
                            printf ("Case #%d: %d\n", a, 4);
                        else
                        {
                            if (n==2 || t[n-3]<=3 || t[n-2]<=4)
                                printf ("Case #%d: %d\n", a, 5);
                            else
                                printf ("Case #%d: %d\n", a, 6);
                        }
                    }
                    else
                    {
                        if (t[n-1]==7)
                        {
                            if (n==1 || t[n-2]<=4)
                                printf ("Case #%d: %d\n", a, 5);
                            else
                            {
                                if (n==2 || t[n-3]<=4 || t[n-2]<=5)
                                    printf ("Case #%d: %d\n", a, 6);
                                else
                                    printf ("Case #%d: %d\n", a, 7);
                            }
                        }
                        else
                        {
                            if (t[n-1]==8)
                            {
                                if (n==1 || t[n-2]<=4)
                                    printf ("Case #%d: %d\n", a, 5);
                                else
                                {
                                    if (n==2 || t[n-3]<=4 || t[n-2]<=5)
                                        printf ("Case #%d: %d\n", a, 6);
                                    else
                                    {
                                        if (n==3 || t[n-4]<=4 || t[n-2]<=6 || t[n-3]<=5)
                                            printf ("Case #%d: %d\n", a, 7);
                                        else
                                            printf ("Case #%d: %d\n", a, 8);
                                    }
                                }
                            }
                            else
                            {
                                if (n==1 || t[n-2]<=3)
                                    printf ("Case #%d: %d\n", a, 5);
                                else
                                {
                                    if (t[n-2]<=5 || (t[n-2]<=6 && (n==2 || t[n-3]<=3)))
                                        printf ("Case #%d: %d\n", a, 6);
                                    else
                                    {
                                        if (n==2 || t[n-3]<=5 || t[n-2]<=6)
                                            printf ("Case #%d: %d\n", a, 7);
                                        else
                                        {
                                            if (n==3 || t[n-4]<=5 || t[n-2]<=7 || t[n-3]<=6)
                                                printf ("Case #%d: %d\n", a, 8);
                                            else
                                                printf ("Case #%d: %d\n", a, 9);
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    return 0;
}
