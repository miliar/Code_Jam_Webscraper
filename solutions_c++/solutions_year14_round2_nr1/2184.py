#include <stdio.h>
#include <string.h>
//#include <string>

//using namespace std;

int main ()
{
    int T, N;
    //string strs[100];
    scanf("%d", &T);
    for (int t = 0; t < T; ++t)
    {
        bool stop = false, feglawon = false;
        scanf("%d", &N);
        /*for (int i = 0; i < N; ++i)
        {
            char tmp[100];
            scanf("%s", tmp);
            strs[i] = tmp;
        }*/
        char a[200];
        char b[200];
        scanf("%s", a);
        scanf("%s", b);
        for (int i = strlen(a); i < 200; ++i)
        {
            a[i] = '\0';
        }
        for (int i = strlen(b); i < 200; ++i)
        {
            b[i] = '\0';
        }

        int j = 0, steps = 0;
        while (!stop)
        {
            if (a[j] == '\0' && b[j] == '\0')
            {
                stop = true;
                break;
            }

            if (a[j] != b[j])
            {
                if (j == 0)
                {
                    stop = true;
                    feglawon = true;
                    break;
                }
                else if (b[j-1] == a[j])
                {
                    int length = strlen(b);
                    for (int i = length; i >= j; --i)
                    {
                        b[i] = b[i-1];
                    }
                    steps++;
                }
                else if (a[j-1] == b[j])
                {
                    int length = strlen(a);
                    for (int i = length; i >= j; --i)
                    {
                        a[i] = a[i-1];
                    }
                    steps++;
                }
                else
                {
                    stop = true;
                    feglawon = true;
                }
            }
            j++;
        }

        if (!feglawon)
        {
            printf("Case #%d: %d\n", t+1, steps);
        }
        else
        {
            printf("Case #%d: Fegla Won\n", t+1);
        }
    }
}