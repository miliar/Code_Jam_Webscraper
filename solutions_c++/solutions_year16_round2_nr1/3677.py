//OUM HARI OUM, OUM TATSAT
// OUM NAMA VAGABATE BASUDEBAY
// OUM NAMA MA SWARASATI OUM NAMA

#include<cmath>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<fstream>
#include<string>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<sstream>
#include<stack>
#include<stdlib.h>
#include<iostream>
#include<algorithm>

#define cl(vctr) vctr.clear()
#define ms(v, ar) memset(ar, v, sizeof(ar))

const double pi=(double)(2.0 * acos( 0.0 ));
const int inf=1 << 30;
const double eps=1E-9;
const double e = exp(1.0);
const int sz=100000 + 5;
const int mod=1000000000 + 7;

using namespace std;
typedef long long int ll;

char s[91];
int d[10],cnt[2001];

int main()
{
    freopen("Ain.in","r",stdin);
    freopen("Aout.in","w",stdout);
    int t,T,i,j;
    scanf("%d",&t);
    T=t;
    while(t--)
    {
        scanf("%s",&s);
        ms(0,cnt);
        ms(0,d);
        for(i=0;s[i];i++)
        {
            cnt[s[i]]++;
        }

        d[0]=cnt['Z'];
        cnt['Z']-=d[0];
        cnt['E']-=d[0];
        cnt['R']-=d[0];
        cnt['O']-=d[0];

        d[2]=cnt['W'];
        cnt['T']-=d[2];
        cnt['W']-=d[2];
        cnt['O']-=d[2];

        d[4]=cnt['U'];
        cnt['F']-=d[4];
        cnt['O']-=d[4];
        cnt['U']-=d[4];
        cnt['R']-=d[4];

        d[3]=cnt['R'];
        cnt['T']-=d[3];
        cnt['H']-=d[3];
        cnt['R']-=d[3];
        cnt['E']-=2*d[3];

        d[5]=cnt['F'];
        cnt['F']-=d[5];
        cnt['I']-=d[5];
        cnt['V']-=d[5];
        cnt['E']-=d[5];

        d[6]=cnt['X'];
        cnt['S']-=d[6];
        cnt['I']-=d[6];
        cnt['X']-=d[6];

        d[7]=cnt['S'];
        cnt['S']-=d[7];
        cnt['E']-=d[7];
        cnt['V']-=d[7];
        cnt['E']-=d[7];
        cnt['N']-=d[7];

        d[8]=cnt['G'];
        cnt['E']-=d[8];
        cnt['I']-=d[8];
        cnt['G']-=d[8];
        cnt['H']-=d[8];
        cnt['T']-=d[8];

        d[9]=cnt['I'];
        cnt['N']-=d[9];
        cnt['I']-=d[9];
        cnt['N']-=d[9];
        cnt['E']-=d[9];

        d[1]=cnt['O'];

        printf("Case #%d: ",T-t);
        for(i=0;i<10;i++)
        {
            for(j=0;j<d[i];j++)
            {
                printf("%d",i);
            }
        }
        printf("\n");
    }

    return 0;
}
