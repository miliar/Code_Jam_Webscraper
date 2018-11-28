#include <stdio.h>
#include <cstring>
#include <iostream>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <vector>
#include <list>
#include <cstdlib>
#include <algorithm>
using namespace std;
typedef long long LL;
#define eps 1e-9
#define M 33333
#define N 31622
char s[1111];
int main(){
  freopen("A.in","r",stdin);
  freopen("A.out","w",stdout);
  int T;
  cin>>T;
  int cases=1;
  while(T--){
    int n;
    cin>>n;
    cin>>s;
    int len=strlen(s);
    int pl=s[0]-'0',ans=0;
    for(int i=1;i<len;i++){
       if(s[i]!='0')
       {
           if(pl < i)
                ans += (i-pl),pl=i+(s[i]-'0');
           else
              pl+=s[i]-'0';
       }
    }
    printf("Case #%d: %d\n",cases++,ans);
  }
}
