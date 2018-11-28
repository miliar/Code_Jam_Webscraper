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
int n,J,ct;
char s[10001];
void Do(){
    scanf("%d%d",&n,&J);
    for(int i=0;i<J;i++){
        printf("11"); ct = i;
        for(int j=0;j<14;j++)
            printf("%d",ct%2), ct /= 2;
        printf("1");
        ct = i;
        for(int j=0;j<14;j++)
            printf("%d",ct%2), ct /= 2;
        printf("1 ");
        printf("3 2 5 2 7 2 3 2 11\n");
    }
}
int main(){
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int rr=1;rr<=T;rr++){
        printf("Case #%d:\n",rr);
        Do();
        printf("\n");
    }
    return 0;
}
