
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
#define MAX         999
typedef long long int LL;
typedef pair<int,int> pii;

string C, J;
bool Cok[MAX+11];
bool Jok[MAX+11];

bool F(string str, int val)
{
    int i = (int) str.size() - 1, d;

    while(i >= 0)
    {
        d = val % 10;
        if(str[i] == '?' || (str[i] - '0') == d);
        else return false;

        val /= 10;
        i--;
    }

    return true;
}

void go(int v)
{
    int cnt = 0;
    while(v)
    {
        cnt++;
        v/=10;
    }

    while(cnt != C.size())
    {
        printf("0");
        cnt++;
    }
}

int main()
{
    freopen("c:\\Users\\User\\Desktop\\B.in", "r", stdin);
    freopen("c:\\Users\\User\\Desktop\\out.txt", "w", stdout);

    int i, j, k, t, cs;
    int mxval, minD;
    int v1, v2;

    sf(t);
    for(cs = 1; cs <= t; cs++)
    {
        memset(Cok, false, sizeof(Cok));
        memset(Jok, false, sizeof(Jok));
        v1 = v2 = -1;

        cin >> C >> J;
        if(C.size() == 1) mxval = 9;
        else if(C.size() == 2) mxval = 99;
        else mxval = 999;

        for(i = 0; i <= mxval; i++)
        {
            Cok[i] = F(C, i);
            Jok[i] = F(J, i);
        }

        minD = (1<<30);
        for(i = 0; i <= mxval; i++)
            for(j = 0; j <= mxval; j++)
                if(Cok[i] && Jok[j])
                    minD = min(minD, abs(i-j));

        for(i = 0; i <= mxval; i++)
            if(Cok[i])
            {
                j = i - minD;
                if(j >= 0 && Jok[j])
                {
                    v1 = i;
                    v2 = j;
                    break;
                }

                j = i + minD;
                if(j <= mxval && Jok[j])
                {
                    v1 = i;
                    v2 = j;
                    break;
                }
            }

        printf("Case #%d: ", cs);

        go(v1);
        if(v1) printf("%d", v1);
        printf(" ");

        go(v2);
        if(v2) printf("%d", v2);
        puts("");
    }
    return 0;
}




