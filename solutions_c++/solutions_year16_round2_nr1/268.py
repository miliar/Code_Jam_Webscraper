
#include<bits/stdc++.h>
using namespace std;
#define D(x)        cout<<#x " = "<<(x)<<endl
#define un(x)       x.erase(unique(x.begin(),x.end()), x.end())
#define sf(n)       scanf("%d", &n)
#define sff(a,b)    scanf("%d %d", &a, &b)
#define sfff(a,b,c) scanf("%d %d %d", &a, &b, &c)
#define pb          push_back
#define mp          make_pair
#define xx          first
#define yy          second
#define hp          (LL) 999983
#define MAX         2000
typedef long long int LL;
typedef pair<int,int> pii;

char str[MAX+11];
int cnt[200];
string nm[15] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int res[15];
int newRes[15];
int finres[15];

void fix(int *arr)
{
    int i, j;
    for(i = 0; i < 10; i++)
        if(arr[i])
            for(j = 0; j < nm[i].size(); j++)
                cnt[nm[i][j]] -= arr[i];
}

int main()
{
    freopen("c:\\Users\\User\\Desktop\\A.in", "r", stdin);
    freopen("c:\\Users\\User\\Desktop\\out.txt", "w", stdout);

    int i, j, k, t, cs;
    int n;

    sf(t);
    for(cs = 1; cs <= t; cs++)
    {
        memset(cnt, 0, sizeof(cnt));
        memset(res, 0, sizeof(res));
        memset(newRes, 0, sizeof(newRes));

        scanf("%s", str+1);
        n = strlen(str+1);

        for(i = 1; i <= n; i++)
            cnt[str[i]]++;

        res[0] = cnt['Z'];
        res[2] = cnt['W'];
        res[4] = cnt['U'];
        res[6] = cnt['X'];
        res[8] = cnt['G'];
        fix(res);

        newRes[1] = cnt['O'];
        newRes[3] = cnt['T'];
        newRes[5] = cnt['F'];
        newRes[7] = cnt['S'];
        fix(newRes);

        res[9] = cnt['E'];
        for(i = 0; i < 10; i++)
            finres[i] = res[i] + newRes[i];

        printf("Case #%d: ", cs);
        for(i = 0; i < 10; i++)
            while(finres[i])
            {
                printf("%d", i);
                finres[i]--;
            }

        puts("");
    }
    return 0;
}




