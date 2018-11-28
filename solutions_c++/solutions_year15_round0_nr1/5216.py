#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t = 0, s = 0, f = 0, tot = 0;
    string str;

    scanf("%d", &t);

    for(int i = 1; i <= t; i++)
    {
        f = 0;
        tot = 0;

        scanf("%d", &s);

        cin>>str;

        for(int i = 0; i <= s; i++)
        {
            switch(str[i])
            {
                case '0':
                    break;
                case '1':
                    if(tot >= i)
                        tot += 1;
                    else
                    {
                        f += (i - tot);
                        tot += (f + 1);
                    }
                    break;
                case '2':
                    if(tot >= i)
                        tot += 2;
                    else
                    {
                        f += (i - tot);
                        tot += (f + 2);
                    }
                    break;
                case '3':
                    if(tot >= i)
                        tot += 3;
                    else
                    {
                        f += (i - tot);
                        tot += (f + 3);
                    }
                    break;
                case '4':
                    if(tot >= i)
                        tot += 4;
                    else
                    {
                        f += (i - tot);
                        tot += (f + 4);
                    }
                    break;
                case '5':
                    if(tot >= i)
                        tot += 5;
                    else
                    {
                        f += (i - tot);
                        tot += (f + 5);
                    }
                    break;
                case '6':
                    if(tot >= i)
                        tot += 6;
                    else
                    {
                        f += (i - tot);
                        tot += (f + 6);
                    }
                    break;
                case '7':
                    if(tot >= i)
                        tot += 7;
                    else
                    {
                        f += (i - tot);
                        tot += (f + 7);
                    }
                    break;
                case '8':
                    if(tot >= i)
                        tot += 8;
                    else
                    {
                        f += (i - tot);
                        tot += (f + 8);
                    }
                    break;
                case '9':
                    if(tot >= i)
                        tot += 9;
                    else
                    {
                        f += (i - tot);
                        tot += (f + 9);
                    }
                    break;
            }
        }

        printf("Case #%d: %d\n", i, f);
    }

    return 0;
}
