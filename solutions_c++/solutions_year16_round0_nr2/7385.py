#include <cstdio>
#include <cstring>
#include <map>
#include <queue>
#include <deque>
#include <algorithm>
#include <iostream>
#include <string>
#include <stack>
using namespace std;
typedef long long LL;
#define MAXN 100


int main()
{
    int T;
    
    freopen("/Users/thedream/Desktop/cpp/cpp/input","r",stdin);
    freopen("/Users/thedream/Desktop/cpp/cpp/output","w",stdout);
    
    scanf("%d",&T);
    
    
    for (int t=1;t<=T;t++) {
        string a;
        cin >> a;
        int ans = 0;
        int len = a.length();
        
        for(int l=len-1;l>=0;l--){
            if(a[l] == '-'){
                for(int i=0;i<=l;i++){
                    if(a[i]=='-') a[i]='+';
                    else a[i] = '-';
                }
                ans++;
            }
        }
        
        printf("Case #%d: %d\n",t,ans);
    }
    
    return 0;
}