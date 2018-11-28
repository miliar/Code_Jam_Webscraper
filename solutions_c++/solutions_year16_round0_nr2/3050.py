#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector>
#include<queue>
#define LL long long
#define maxn 100100
#define inf 0x3f3f3f3f
#define IN freopen("in.txt","r",stdin);
using namespace std;


int main(int argc, char const *argv[])
{
    IN;
    freopen("out.txt","w",stdout);

    int t,ca=1; cin >> t; getchar();
    while(t--)
    {
        int ans = 0;
        int flag = 0;
        char c = getchar();
        if(c == '-') ans = 1;
        if(c == '+') flag = 1;

        while((c=getchar())!='\n'){
            if(c == '+') flag = 1;
            if(c == '-' && flag) ans+=2,flag=0;
        }
        printf("Case #%d: %d\n",ca++,ans);
    }

    return 0;
}
