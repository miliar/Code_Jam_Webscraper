#include <iostream>
#include <algorithm>
#include <cstdio>
#include <queue>
#include <math.h>
#include <limits.h>
#include <cstdlib>
#include <string.h>
#include <vector>
#include <map>
using namespace std;
//mehulagarwal
#define ll         long long
#define S(x)       scanf("%d", &x)
#define Sl(x)      scanf("%lld", &x)
#define Sd(x)      scanf("%lf", &x)
#define P(x)       printf("%d\n", x)
#define Pl(x)      printf("%lld\n", x)
#define Pd(x)      printf("%lf\n", x)
#define Pblank()   printf(" ")
#define mem(x,y)   memset(x,y,sizeof(x))
#define F(x,y,z,i) for (x = y; x < z; x = x + i)
#define mod 1000000007

//char s[1005];

int main()
{
    int cid,i,t,peop,ans,len;
    char s[1005];
    FILE *fi,*fo;
    fi = fopen("inp_a.txt","r");
    fo = fopen("out_a.txt","w+");
   // scanf("%d", &t);
    fscanf(fi,"%d", &t);
    //freopen("inp.txt","r",stdin);

    for (cid = 1; cid <= t; cid++) {
        //fscanf(fo,"%s",s);
        fscanf(fi,"%d", &len);
        ans = 0;
        peop = 0;
      //  cin >> s;
        fscanf(fi,"%s",s);
        for (i = 0; i <= len; i++) {
            if (peop < i) {
                ans++;
                peop++;
            }
            peop = peop + (s[i] - '0');
        }
        fprintf(fo,"Case #%d: %d\n",cid,ans);
    }


	return 0;
}
