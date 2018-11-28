/*
ID: jsnjhcb1
PROG: c
LANG: C++
*/
/*************************************************************************
	> File Name: c.cpp
	> Author: UCU
	> Mail: jsnjhcb@icloud.com
	> Created Time: 六  4/ 9 19:52:00 2016
 ************************************************************************/

#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cctype>
#include<vector>
#include<map>
#include<set>
#include<stack>
#include<list>
#include<string>
#include<cstdlib>
#include<queue>
#include<cmath>
#include<iomanip>
#include<climits>
#include<fstream>
using namespace std;
int ans[50];
int n,j;
int s[50];
bool judge(int *s){
    bool flag;
    for(int i=2;i<=10;++i){
        long long tmp = 0;
        flag = false;
        for(int k=0;k<n;++k){
            tmp *= (long long)i;
            tmp += (long long)s[k];
        }
        for(long long t = 2; t * t <= tmp ;++t){
            if(tmp%t==0){
                flag = true;
                ans[i] = t;
                break;
            }
        }
        if(!flag) return false;
    }
    return true;
}
int cnt = 0;
void dfs(int index){
    if(cnt == j) return ;
    if(index == n-1){
        if(judge(s)){
            cnt ++;
            for(int i=0;i<n;++i){
                printf("%d",s[i]);
            }
            for(int i=2;i<=10;++i){
                printf(" %d",ans[i]);
            }
            printf("\n");
        }
    }
    else{
        s[index] = 0;
        dfs(index+1);
        s[index] = 1;
        dfs(index+1);
    }
}
int main(){
    int T;
    scanf("%d",&T);
    for(int ca = 1 ; ca <= T; ++ ca){
        printf("Case #%d:\n",ca);
        scanf("%d%d",&n,&j);
        cnt = 0;
        s[0] = s[n-1] = 1;
        dfs(1);
    }
}
