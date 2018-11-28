/*******************************************************************
** AUTHOR   : Wenzheng jiang
** EMAIL    : jwzh.hi@gmail.com 
** OS       : ArchLinux 
** EDITER   : VIM
******************************************************************/
#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>

using namespace std;

#define pf(x) printf("%d\n",x)
#define pf2(x,y) printf("%d %d\n",x,y)
#define pf3(x,y,z) printf("%d %d %d\n",x,y,z)
#define pf4(x,y,z,k)printf("%d %d %d %d\n",x,y,z,k)
#define sf(x) scanf("%d",&x)
#define sf2(x,y) scanf("%d%d",&x,&y)
#define sf3(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define sf4(x,y,z,k) scanf("%d%d%d%d",&x,&y,&z,&k)
typedef long long ll;
double const eps = 1e-6;
const int inf = 0x3fffffff;
const int size = 10000000 + 5;
int paliSum[size];
int pali[size];
bool ispali(ll n)
{
    char str[20];
    sprintf(str,"%lld",n);
    int len = strlen(str);
    for(int i = 0,j = len-1; i < j; i++,j--)
        if(str[i] != str[j]) return false;
    return true;
}
void make_table()
{
    paliSum[1] = 1;
    for(int i = 2; i < 10000000; i++){
        ll n = i;
        if(ispali(n) && ispali(n*n))
            paliSum[n] = paliSum[n-1] + 1;
        else paliSum[n] = paliSum[n-1];
    }
}
int cal(ll n)
{
    ll i;
    for(i = sqrt(1.0*n) - 1; i*i <= n; i++)
        ;
    return i-1;
}
int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int t,ncase = 0;
    make_table();
    sf(t);
    while(t--){
        ll a,b;
        cin >> a >> b;
//        cout << cal(a) << ' ' << cal(b) << endl;
        printf("Case #%d: %d\n",++ncase,paliSum[cal(b)] - paliSum[cal(a-1)]);
    }
}

