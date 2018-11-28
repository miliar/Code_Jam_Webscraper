#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

#define ff first
#define ss second

int main()
{
    freopen("D.in","r",stdin);
    freopen("out2.txt","w",stdout);
    //test("");
    int t;
    scanf("%d",&t);
    for(int I=1;I<=t;I++){
      int k,c,s;
      cin >> k >> c >> s;
      printf("Case #%d: ",I);
      for(int i=1;i<=k;i++)cout << i << " ";
      cout << "\n";
    }
    return 0;
}
