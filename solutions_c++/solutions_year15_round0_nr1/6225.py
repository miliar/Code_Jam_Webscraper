#include<cstdio>
#include<algorithm>

using namespace std;

char txt[1005];
int n;

int main()
{
    int testy;
    scanf("%d", &testy);
    for( int numer=1; numer<=testy; numer++)
    {
        scanf("%d%s", &n, &txt);
        int mam = txt[0] - '0', dodalem=0;
        for( int i=1; i<=n; ++i)
        {
            if( mam < i) {
                dodalem += i-mam;
                mam = i;
            }
            mam+=txt[i]-'0';
        }
        printf("Case #%d: %d\n", numer, dodalem);
    }
}
