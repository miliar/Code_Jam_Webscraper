//
//  main.cpp
//  GCJ.2013.1
//
//  Created by Orpine on 13-4-13.
//  Copyright (c) 2013年 Orpine. All rights reserved.
//

#include <iostream>

int T;
long long L,R,ret;
int ch[20],ans,tot;

bool Check2(long long num)
{
    int c[20],cnt = 0;
    while(num)
    {
        c[++cnt] = num%10;
        num /= 10;
    }
    for(int i = 1,tmp = cnt; i < tmp;i++,tmp--)
    {
        if (c[i] != c[tmp]) {
            return false;
        }
    }
    return true;
}
void Calc(int len)
{
    long long ret = 0;
    for (int i = 1; i <= len; i++) {
        ret = ret * 10 + ch[i];
    }
    ret = ret * ret;
    if (Check2(ret) && ret >= L && ret <= R) {
        ans++;
    }
}
void Check(int n)
{
    int len = n << 1;
    for (int i = 1; i <= n; i++) {
        ch[len] = ch[i]; len--;
    }
    Calc(n << 1);
    len = n * 2 - 1;
    for (int i = 1; i < n; i++) {
        ch[len] = ch[i]; len--;
    }
    Calc(n * 2 - 1);
}
void DFS(int st)
{
    if(st >= tot)return;
    if (st == 1) {
        for (int i = 1; i <= 9; i++) {
            ch[st] = i;
            Check(st);
            DFS(st + 1);
        }
    }
    else{
        for (int i = 0; i <= 9; i++) {
            ch[st] = i;
            Check(st);
            DFS(st + 1);
        }
    }
}
void Work()
{
    ans = 0;tot = 0;
    scanf("%lld%lld",&L,&R);
    long long r = R;
    while(r){++tot;r /= 10;}
    tot++;
    tot >>= 1;tot++;
    DFS(1);
    printf("%d\n",ans);
}
int main(int argc, const char * argv[])
{
//    freopen("t3.in","r",stdin);
//    freopen("t3.out","w",stdout);
    scanf("%d",&T);
    for (int i = 1; i <= T; i++) {
        printf("Case #%d: ",i);
        Work();
    }
    return 0;
}

