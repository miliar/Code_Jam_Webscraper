#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 105;
int ar[MAXN][MAXN];
int mxh[MAXN];
int mxv[MAXN];
int main()
{
int t;
cin >> t;
for(int i=1; i<=t; i++)
{
    int h,w;
    cin >> h >> w;
    for(int j=0;j<h; j++)
    for(int k=0; k<w; k++)
      cin >> ar[j][k];
    memset(mxh, 0, sizeof(mxh));
    memset(mxv, 0, sizeof(mxv));
    for(int j=0; j<h; j++)
      for(int t=0; t<w; t++){
        mxh[j]=max(mxh[j], ar[j][t]);
        mxv[t]=max(mxv[t], ar[j][t]);
      }
    bool g = true;
    for(int j=0; j<h; j++)
      for(int t=0; t<w; t++)if(min(mxh[j],mxv[t])!=ar[j][t])g = false;
    cout << "Case #" << i<<": ";
    if(g)cout << "YES\n"; else cout << "NO\n"; 
}
return 0;
}
