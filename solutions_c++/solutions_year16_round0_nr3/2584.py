#include<cstdio>
#include <cstring>

#define mod 1000000007
#define inf 1000000009
#define MX 100000001

#define pb push_back
#define mp make_pair
#define ll long long
#define gc getchar
#define vi vector<int>
#define rep(i, n) for(int i=0; i<n; i++)

using namespace std;
int pr[5761457];
bool ispr[MX], bin[16];
ll div[10];

int main() {
	#ifndef ONLINE_JUDGE
    //freopen("C:\\Users\\yashvir\\Downloads\\B-large.in","r",stdin);
    freopen("C:\\Users\\yashvir\\Downloads\\C-small-attempt0.in","r",stdin);
    //freopen("in.txt","r",stdin);
    freopen("out.txt", "w", stdout);
    #endif // ONLINE_JUDGE
    int t, k=0, j, I, m, a;
    int gf, n, i, d, np;
    ll s, p, v;
    for(I=2; I<MX; I++)
    {
        if(ispr[I]) continue;
        pr[k++]=I;
        for(j=2*I; j<MX; j+=I) ispr[j]=true;
    }
    np=k;

    scanf("%d", &t);
    for(I=1; I<=t; I++)
    {
         scanf("%d%d", &n, &j);
         printf("Case #%d:\n", I);
         n-=2;
         m=1<<n-2; d=j;
         for(i=0; i<m; i++)
         {
             gf=1;
             for(k=2; k<11; k++)
             {
                 s=1;
                 p=k;
                 for(j=0; j<n; j++)
                 {
                     if(i&(1<<j)) { s+=p; bin[j]=1; }
                     else bin[j]=0;
                     p*=k;
                 }
                 s+=p; p=1;
                 for(j=0; j<np; j++)
                 {
                     v=pr[j];
                     if(v*v>s) break;
                     if(s%v==0) {p=0; break;}
                 }
                 if(p==1) { gf=0; break; }
                 div[k]=v;
             }
             if(gf)
             {
                 d--;
                 printf("1");
                 for(j=n-1; j>=0; j--) printf("%d", bin[j]);
                 printf("1");
                 for(j=2; j<11; j++) printf(" %lld", div[j]);
                 printf("\n");
                 if(d==0) break;
             }
         }
    }

    return 0;
}
