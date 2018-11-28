#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

int a[5][5];

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    a[1][1] = 1;
    a[1][2] = 2;
    a[1][3] = 3;
    a[1][4] = 4;
    a[2][1] = 2;
    a[2][2] = -1;
    a[2][3] = 4;
    a[2][4] = -3;
    a[3][1] = 3;
    a[3][2] = -4;
    a[3][3] = -1;
    a[3][4] = 2;
    a[4][1] = 4;
    a[4][2] = 3;
    a[4][3] = -2;
    a[4][4] = -1;

    int t = 0, l = 0, m = 0, x = 0, r = 0, f = 0;
    string str;

    scanf("%d", &t);

    for(int k = 1; k <= t; k++)
    {
        m = 0;
        r = 0;
        f = 0;

        scanf("%d%d", &l, &x);

        cin>>str;

        switch(str[0])
        {
            case 'i':
                r = 2;
                break;
            case 'j':
                r = 3;
                break;
            case 'k':
                r = 4;
                break;
        }

        for(int i = 1; str[i] != '\0'; i++)
        {
            switch(str[i])
            {
                case 'i':
                    m = 2;
                    break;
                case 'j':
                    m = 3;
                    break;
                case 'k':
                    m = 4;
                    break;
            }

            if(r < 0)
                r = -1 * a[-r][m];
            else
                r = a[r][m];
        }

        m = r;

        for(int i = 2; i <= x; i++)
        {
            if(m < 0 && r < 0)
                m = a[-m][-r];
            else
            if(m < 0 && r >= 0)
                m = -1 * a[-m][r];
            else
            if(m >= 0 && r < 0)
                m = -1 * a[m][-r];
            else
                m = a[m][r];
        }

        if(m == -1)
        {
            string res = str;

            for(int i = 1; i < x; i++)
                res += str;

            switch(res[0])
            {
                case 'i':
                    r = 2;
                    break;
                case 'j':
                    r = 3;
                    break;
                case 'k':
                    r = 4;
                    break;
            }

            for(int i = 1; res[i] != '\0'; i++)
            {
                f = 0;

                if(r == 2)
                {
                    int r1 = 0;

                    switch(res[i])
                    {
                        case 'i':
                            r1 = 2;
                            break;
                        case 'j':
                            r1 = 3;
                            break;
                        case 'k':
                            r1 = 4;
                            break;
                    }

                    for(int j = i + 1; res[j] != '\0'; j++)
                    {
                        if(r1 == 3)
                        {
                            int r2 = 0;

                            switch(res[j])
                            {
                                case 'i':
                                    r2 = 2;
                                    break;
                                case 'j':
                                    r2 = 3;
                                    break;
                                case 'k':
                                    r2 = 4;
                                    break;
                            }

                            for(int l = j + 1; res[l] != '\0'; l++)
                            {
                                switch(res[l])
                                {
                                    case 'i':
                                        m = 2;
                                        break;
                                    case 'j':
                                        m = 3;
                                        break;
                                    case 'k':
                                        m = 4;
                                        break;
                                }

                                if(r2 < 0)
                                    r2 = -1 * a[-r2][m];
                                else
                                    r2 = a[r2][m];
                            }

                            if(r2 == 4)
                            {
                                f = 1;
                                break;
                            }
                        }
                        else
                        {
                            switch(res[j])
                            {
                                case 'i':
                                    m = 2;
                                    break;
                                case 'j':
                                    m = 3;
                                    break;
                                case 'k':
                                    m = 4;
                                    break;
                            }

                            if(r1 < 0)
                                r1 = -1 * a[-r1][m];
                            else
                                r1 = a[r1][m];
                        }

                        if(f == 1)
                        {
                            f = 1;
                            break;
                        }
                    }
                }
                else
                {
                    switch(res[i])
                    {
                        case 'i':
                            m = 2;
                            break;
                        case 'j':
                            m = 3;
                            break;
                        case 'k':
                            m = 4;
                            break;
                    }

                    if(r < 0)
                        r = -1 * a[-r][m];
                    else
                        r = a[r][m];
                }

                if(f == 1)
                    break;
            }

            if(f == 1)
                printf("Case #%d: YES\n", k);
            else
                printf("Case #%d: NO\n", k);
        }
        else
            printf("Case #%d: NO\n", k);
    }

    return 0;
}
