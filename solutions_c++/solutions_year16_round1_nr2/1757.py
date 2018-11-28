#include <iostream>
#include <cstdio>
#include <map>
#include <algorithm>

using namespace std;

void solve(int n,int num)
{
    map<int,int> stat;
    int res[51]={0};
    int mar[101][51];
    for(int i=0;i<n*2-1;i++){
        for(int j=0;j<n;j++){
            scanf("%d",&mar[i][j]);
            stat[mar[i][j]]++;
        }
    }
    int i=0;
    for(auto iter:stat){
        if((int)(iter.second)%2!=0)res[i++]=iter.first;
    }
    sort(res,res+n);
    printf("Case #%d:",num+1);
    for(i=0;i<n;i++){
        printf(" %d",res[i]);
    }
    printf("\n");
}

int main()
{
    //freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=0;i<t;i++){
        int n;
        scanf("%d",&n);
        solve(n,i);
    }
    return 0;
}
