#include<cstdio>
#include<algorithm>
#include<iostream>
#include<vector>
#include<set>
#include<map>
#include<cmath>
#include<string>
#include<cstring>
#include<bitset>
#define pii pair<int,int>
#define A first
#define B second
using namespace std;
int n,ct;
char s[10001];
void Do(){
    scanf("%s",s);
    n = 0; ct = 1;
    for(int i=0;s[i]!='\0';i++){
        n++;
        if(i > 0 && s[i] != s[i-1]) ct++;
    }
    if(s[n-1] == '+') ct--;
    printf("%d",ct);
}
int main(){
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int rr=1;rr<=T;rr++){
        printf("Case #%d: ",rr);
        Do();
        printf("\n");
    }
    return 0;
}
