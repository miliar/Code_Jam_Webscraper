#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
int t,k,c,s;
int kount;

void solve()
{
    printf("Case #%d:",++kount);
    for(int i =1 ;i<=s; i++){
        printf(" %d",i);
    }
    printf("\n");
}

int main()
{
    freopen("D-small-attempt2.in","r",stdin);
    freopen("1.txt","w",stdout);
    scanf("%d",&t);
    while(t--){
        scanf("%d%d%d",&k,&c,&s);
        solve();
    }
    return 0;
}
