#include <iostream>
#include <algorithm>
#include <string>
#include <stdio.h>
#include <cstring>
#include <vector>
using namespace std;
typedef long long LL;
#define S 1005
int n,t,txt;
vector<int>p;
vector<LL>ok;
char ch[17];
LL a,b;
bool isPalindrome(LL v)
{
    memset(ch, 0, sizeof ch);
    sprintf(ch,"%lld",v);
    int len = strlen(ch);
    for(int i = 0; i < len/2; ++i)if(ch[i] != ch[len - i - 1])return false;
    return true;
}
int main()
{
    freopen("1.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int i,j,k;
    for(int i = 1; i <= 10000000; ++i)if(isPalindrome(i))
    {
        LL num = i;
        num = num * i;
        if(isPalindrome(num))ok.push_back(num);
    }
    scanf("%d",&t);
    while(t--)
    {
        cin >> a >> b;
        int ans = 0;
        for(int i = 0; i < ok.size(); ++i)
        {
            if(ok[i] >= a && ok[i] <= b)ans++;
        }
        printf("Case #%d: %d\n",++txt,ans);
    }
    return 0;
}
