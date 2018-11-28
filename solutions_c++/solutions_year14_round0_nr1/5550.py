#include <iostream>
#include <cstdio>

using namespace std;

int a[4][4];
bool ok[17];

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);

    int t;
    scanf("%i", &t);
    for(int _ = 0; _ < t; _++)
    {
        for(int i = 1; i <= 16; i++) ok[i] = true;
        for(int __ = 0; __ < 2; __++)
        {
            int ans;
            scanf("%i", &ans);
            for(int i = 0; i < 4; i++)
                for(int j = 0; j < 4; j++)
                {
                    int x;
                    scanf("%i", &x);
                    if(i + 1 != ans) ok[x] = false;
                }
        }

        int cnt = 0;
        for(int i = 1; i <= 16; i++) cnt += ok[i];
        printf("Case #%i: ", _ + 1);
        if(cnt > 1) printf("Bad magician!\n");
        else if(cnt == 0) printf("Volunteer cheated!\n");
        else for(int i = 1; i <= 16; i++) if(ok[i]) printf("%i\n", i);
    }
    return 0;
}
