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
        cin>>n;
        foru(i,0,n) scanf("%i",&a[i]);
        int res=1000000000;
        foru(time,1,1001) {
            int ans=time;
            foru(i,0,n) ans+=(a[i]-1)/time;
            res=min(res,ans);
        }
        printf("Case #%i: %i\n",test+1,res);
    }
    fclose(stdin);
    fclose(stdout);
    re 0;
}
