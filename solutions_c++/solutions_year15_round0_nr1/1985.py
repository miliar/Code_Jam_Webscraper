#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
using namespace std;
#define foru(i,l,r) for(int i=l;i<r;i++)
#define ford(i,l,r) for(int i=l;i>r;i--)
#define ll long long
#define re return
#define pb push_back

const int maxN=1e3+100;
char s[maxN];
int a[maxN],n;

int main() {
    freopen("input.inp","r",stdin);
    freopen("output.out","w",stdout);
    int t;
    scanf("%i\n",&t);
    foru(test,0,t) {
        scanf("%i %s\n",&n,s);
        foru(i,0,n+1) a[i]=s[i]-'0';
        ll sum=a[0];
        ll res=0;
        foru(i,1,n+1) {
            res+=max(1ll*0,i-sum);
            sum=max(1ll*i,sum)+a[i];
        }
        printf("Case #%i: %I64d\n",test+1,res);
    }
    fclose(stdin);
    fclose(stdout);
    re 0;
}
