#include <bits/stdc++.h>

using namespace std;

const char number[][100]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
char ch[2050];
int cnt[30];
int ans[10];

void minu(int x)
{
    ans[x]++;
    for(int i=0;number[x][i];i++)cnt[number[x][i]-'A']--;
}

bool find(int x)
{
    int co[30];
    memset(co,0,sizeof co);
    for(int i=0;number[x][i];i++)
    {
        co[number[x][i]-'A']++;
    }
    for(int i=0;i<26;i++)
    {
        if(co[i]>cnt[i])return false;
    }
    return true;
}

void solve()
{
    scanf("%s",ch);
    memset(ans,0,sizeof ans);
    static int cas=1;
    printf("Case #%d: ",cas++);
    memset(cnt,0,sizeof cnt);
    for(int i=0;ch[i];i++)
    {
        cnt[ch[i]-'A']++;
    }


    while(find(0))minu(0);
    while(find(2))minu(2);
    while(find(8))minu(8);
    while(find(3))minu(3);
    while(find(4))minu(4);
    while(find(5))minu(5);
    while(find(7))minu(7);
    while(find(1))minu(1);
    while(find(6))minu(6);
    while(find(9))minu(9);


    for(int i=0;i<10;i++)
    {
        for(int j=0;j<ans[i];j++)printf("%d",i);
    }
    puts("");



}

int main()
{

#ifdef LOCAL
freopen("A-small-attempt0.in","r",stdin);
freopen("out","w",stdout);
#endif // LOCAL
    int t;
    scanf("%d",&t);
    while(t--)solve();
    return 0;
}
