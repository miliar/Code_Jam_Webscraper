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
#define MAX 100005
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
int main(){//while(1){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int test,x,r,c,k=1;
    sd(test);
    while(test--){
        sd(x);sd(r);sd(c);
        if(r==1){
            if(c==1){
                if(x==1)
                    printf("Case #%d: GABRIEL\n",k);
                else
                    printf("Case #%d: RICHARD\n",k);
            }
            else if(c==2){
                if(x==1 || x==2)
                    printf("Case #%d: GABRIEL\n",k);
                else
                    printf("Case #%d: RICHARD\n",k);
            }
            else if(c==3){
                if(x==1)
                    printf("Case #%d: GABRIEL\n",k);
                else
                    printf("Case #%d: RICHARD\n",k);
            }
            else if(c==4){
                if(x==1 || x==2)
                    printf("Case #%d: GABRIEL\n",k);
                else
                    printf("Case #%d: RICHARD\n",k);
            }
        }
        else if(r==2){
            if(c==1){
                if(x==1 || x==2)
                    printf("Case #%d: GABRIEL\n",k);
                else
                    printf("Case #%d: RICHARD\n",k);
            }
            else if(c==2){
                if(x==1 || x==2)
                    printf("Case #%d: GABRIEL\n",k);
                else
                    printf("Case #%d: RICHARD\n",k);
            }
            else if(c==3){
                if(x==1 || x==2 || x==3)
                    printf("Case #%d: GABRIEL\n",k);
                else
                    printf("Case #%d: RICHARD\n",k);
            }
            else if(c==4){
                if(x==1 || x==2)
                    printf("Case #%d: GABRIEL\n",k);
                else
                    printf("Case #%d: RICHARD\n",k);
            }
        }
        else if(r==3){
            if(c==1){
                if(x==1)
                    printf("Case #%d: GABRIEL\n",k);
                else
                    printf("Case #%d: RICHARD\n",k);
            }
            else if(c==2){
                if(x==1 || x==2 || x==3)
                    printf("Case #%d: GABRIEL\n",k);
                else
                    printf("Case #%d: RICHARD\n",k);
            }
            else if(c==3){
                if(x==1 || x==3)
                    printf("Case #%d: GABRIEL\n",k);
                else
                    printf("Case #%d: RICHARD\n",k);
            }
            else if(c==4){
                if(x==1 || x==2 || x==3 || x==4)
                    printf("Case #%d: GABRIEL\n",k);
                else
                    printf("Case #%d: RICHARD\n",k);
            }
        }
        else if(r==4){
            if(c==1){
                if(x==1 || x==2)
                    printf("Case #%d: GABRIEL\n",k);
                else
                    printf("Case #%d: RICHARD\n",k);
            }
            else if(c==2){
                if(x==1 || x==2)
                    printf("Case #%d: GABRIEL\n",k);
                else
                    printf("Case #%d: RICHARD\n",k);
            }
            else if(c==3){
                if(x==1 || x==2 || x==3 || x==4)
                    printf("Case #%d: GABRIEL\n",k);
                else
                    printf("Case #%d: RICHARD\n",k);
            }
            else if(c==4){
                if(x==1 || x==2 || x==4)
                    printf("Case #%d: GABRIEL\n",k);
                else
                    printf("Case #%d: RICHARD\n",k);
            }
        }
        k++;
    }
    return 0;
}
