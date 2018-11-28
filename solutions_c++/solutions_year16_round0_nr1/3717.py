#include <iostream>
#include <cstring>

using namespace std;


bool checkflag(bool * flag)
{
    bool retval = true;
    for (int i = 0; i < 10; i++)
    {
        retval = (retval && flag[i]);

    }

    return retval;
}

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A_small.out","w",stdout);
    int times;
    cin >> times;
    for (int time = 1; time <= times; time ++)
    {
        bool flag[10];
        memset(flag,false,sizeof(flag));
        int n;
        scanf("%d",&n);
        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", time);
            continue;
        }
        int nn = n;
        do {
            int temp = n;
            while (temp != 0) {
                flag[temp % 10] = true;
                temp = temp / 10;
            }
            n += nn;
        }while (!checkflag(flag));
        n -= nn;
        printf("Case #%d: %d\n",time,n);
    }
    fclose(stdout);
}