#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<string>
#include<cstring>
#include<map>
#include<queue>
#include<vector>
using namespace std;
#define LL long long

int solve(string str){
    int res=0;
    int len=str.size();
    for(int i=len-1;i>=0;--i){
        if(str[i]=='-'){
            res++;
            int inx=i;
            while(inx>=0&&str[inx]=='-'){
                str[inx]='+';inx--;
            }
            for(int j=inx;j>=0;j--){
                if(str[j]=='-')str[j]='+';
                else str[j]='-';
            }
        }
    }
    return res;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    int cas=0;
    while(t--){
        string str;
        cin>>str;
        cas++;
        int ans=solve(str);
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
