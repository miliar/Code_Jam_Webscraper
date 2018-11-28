//Przemysław Jakub Kozłowski
#include <iostream>
#include <cstdio>
#include <algorithm>
#define FI first
#define SE second
#define MP make_pair
using namespace std;
typedef long long LL;
const int N = 103, W = 11, INF = 1000000009;

int sufdziel(int a, int b) {return a/b+(a%b!=0?1:0);}

int t;
int n, P, Q;
int H[N], G[N];
int NIE[N], TAK[N]; // moje

int taba_[N*W+7], tabb_[N*W+7];
int *taba = taba_, *tabb = tabb_;

int main()
{
    scanf("%d", &t);
    for(int ti = 1;ti <= t;ti++)
    {
        scanf("%d%d%d", &P, &Q, &n);

        for(int i = 1;i <= n;i++)
            scanf("%d%d", &H[i], &G[i]);

        for(int i = 1;i <= n;i++)
        {
            int tmp,tmp2;

            tmp = sufdziel(H[i],Q);
            //NIE[i] = MP(-tmp,tmp);
            NIE[i] = tmp;

            //tmp2 = max(1, sufdziel((H[i]-1)%Q,P));
            //tmp = max(0,H[i]-P*(tmp2-1)-1)/Q;
            tmp = (H[i]-1)/Q;
            tmp2 = sufdziel(H[i]-tmp*Q, P);
            //cerr << "TMP2: " << tmp2 << " TMP: " << tmp << endl;
            TAK[i] = tmp-tmp2;
            //TAK[i] = MP(-tmp,tmp-tmp2);

            //cerr << "TI: " << ti << " H[i]: " << H[i] << " P: " << P << " Q: " << Q << " TAK[i]: " << TAK[i] << endl;
            //cerr << "I: " << i << " NIE[i]: " << NIE[i] << " TAK[i]: " << TAK[i] << endl;
        }

        for(int i = 0;i <= N*W;i++) taba[i] = tabb[i] = -INF;

        tabb[1] = 0;

        for(int i = 1;i <= n;i++)
        {
            swap(taba, tabb);

            //cerr << "I: " << i << endl;

            for(int j = 0;j <= N*W;j++) tabb[i] = -INF;

            for(int j = 0;j <= N*W;j++)
                if(taba[j] >= 0)
                {
                    if(j+NIE[i] > N*W || j+TAK[i] > N*W) cerr << "ERROR" << j << " NIE[i]: " << NIE[i] << " TAK[i]: " << TAK[i] << endl;
                    if(taba[j] > tabb[j+NIE[i]])
                        tabb[j+NIE[i]] = taba[j];
                    if(j+TAK[i] >= 0 && taba[j]+G[i] > tabb[j+TAK[i]])
                        tabb[j+TAK[i]] = taba[j]+G[i];
                }

            for(int j = 0;j <= N*W;j++)
                if(tabb[j] < 0)
                    tabb[j] = -INF;
        }

        int wyn = 0;
        for(int i = 0;i <= N*W;i++)
            wyn = max(wyn, tabb[i]);

        printf("Case #%d: %d\n", ti, wyn);
    }
    return 0;
}
