#include<bits/stdc++.h>
#include<unistd.h>
using namespace std ;
#define ll long long
#define N 200100
#define R 0
#define P 1
#define S 2
#define inf 0x3f3f3f3f
int n;
string k[]={"R","P","S"};
int c[3][3]={{0,2},{1,0},{2,1}};
int a[3],b[3];
string gao(int n, int i,int j){
    if (n==1){
        b[i]--;
        b[j]--;
        if (b[i]<0 || b[j]<0) return "Z";
        if (k[i]>k[j]) return k[j]+k[i];
        else return k[i]+k[j];
    }
    string ans1=gao(n-1,c[i][0],c[i][1]);
    string ans2=gao(n-1,c[j][0],c[j][1]);
    if (ans1=="Z" || ans2=="Z") return "Z";
    if (ans1<ans2) return ans1+ans2;
    else return ans2+ans1;
}
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int T,cas=0;
    cin>>T;
    while (T--){
        cin>>n>>a[R]>>a[P]>>a[S];
        b[R]=a[R];b[P]=a[P];b[S]=a[S];
        string ans="Z";
        string ret=gao(n,0,1);
        ans=min(ans,ret);
        b[R]=a[R];b[P]=a[P];b[S]=a[S];
        ret=gao(n,0,2);
        ans=min(ans,ret);
        b[R]=a[R];b[P]=a[P];b[S]=a[S];
        ret=gao(n,1,2);
        ans=min(ans,ret);
        printf("Case #%d: ",++cas);
        if (ans=="Z") puts("IMPOSSIBLE");
        else puts(ans.c_str());
    }
}
