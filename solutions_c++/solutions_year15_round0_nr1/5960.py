/*
    xxx_joker/codersumit
*/
#include <bits/stdc++.h>
#define bitcnt(x) __builtin_popcountll(x)
#define sd(a) scanf("%d",&a)
#define sld(a) scanf("%lld",&a)
#define ss(a) scanf("%s",a)
#define sc(a) scanf("%c",&a)
#define pd(a) printf("%d",a)
#define ps(a) printf("%s",a)
#define pc(a) printf("%c",a)
#define space printf(" ");
#define nw printf("\n")
#define pb push_back
#define FOR(i,a,b) for(i=a;i<b;i++)
#define FORR(i,a,b) for(i=a;i>=b;i--)
#define all(v) v.begin(),v.end()
#define MAX 1005
#define MAXX 1<<13
#define inf 1e9
#define mod 1000000007

typedef long long ll;
typedef unsigned long long ull;
using namespace std;
inline void fastread(int *a)
{
 register char c=0;
 while (c<33) c=getchar();
 *a=0;
 while (c>33)
 {
     *a=*a*10+c-'0';
     c=getchar();
 }
}
char arr[MAX];
int main(){//while(1){
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    int ans,i,test,omax,cnt=0,temp,k;
    sd(test);
    k=1;
    while(test--){
        cnt=ans=0;
        sd(omax);
        ss(arr);
        FOR(i,0,omax+1){
            temp=0;
            if(cnt>=i);
            else{
                temp=(i-cnt);
                ans+=temp;
            }
            cnt+=(int)(arr[i]-'0');
            cnt+=temp;
        }
        printf("Case #%d: %d\n",k,ans);
        k++;
    }
    return 0;
}
