#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;
int t,num;
string s;

void solve()
{
    int len = s.length();
    int kount = 0;
    for(int i=0;i<len;i++){
        if(s[i] == s[i+1]) continue;
        if (s[i]=='+' && i == len -1) break;
        kount ++;
        if(i == len-1) break;
    }
    printf("Case #%d: %d\n",++num,kount);
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("2.txt","w",stdout);
    cin >> t;
    while(t--){
        cin >> s;
        solve();
    }
    return 0;
}
