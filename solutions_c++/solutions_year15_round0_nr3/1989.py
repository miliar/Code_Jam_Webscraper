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

const int maxN=1e4+100;
char s[maxN];
int a[maxN],lef[maxN],rig[maxN],n,m;
bool ok1[10],ok2[10];

int mt[4][4];

//const int mt_={{1,2,3,4},{2,-1,4,-3},{3,-4,-1,2},{4,3,-2,-1}};

int cal(int x,int y) {
    int tx=abs(x);
    int ty=abs(y);
    if (x<0==y<0) re mt[tx-1][ty-1]; else re -mt[tx-1][ty-1];
}

void init() {
    foru(i,0,4) mt[0][i]=mt[i][0]=i+1;
    foru(i,1,4) mt[i][i]=-1;
    mt[1][2]=4;
    mt[1][3]=-3;
    mt[2][1]=-4;
    mt[2][3]=2;
    mt[3][1]=3;
    mt[3][2]=-2;
}

int main() {
    freopen("input.inp","r",stdin);
    freopen("output.out","w",stdout);
    init();
    int t;
    scanf("%i\n",&t);
    foru(test,0,t) {
        printf("Case #%i: ",test+1);
        scanf("%i%i\n",&n,&m);
        scanf("%s",s);
        foru(i,0,n) if (s[i]=='1') a[i]=1; else a[i]=s[i]-'i'+2;
        lef[0]=a[0];
        foru(i,1,n) lef[i]=cal(lef[i-1],a[i]);
        rig[n-1]=a[n-1];
        ford(i,n-2,-1) rig[i]=cal(a[i],rig[i-1]);
        int s=lef[n-1];
        foru(i,1,m) s=cal(s,lef[n-1]);
        if (s!=-1) {
            printf("NO\n");
            continue;
        }
        int d1=0, q1=-1;
        foru(i,0,n) if (lef[i]==2) {
            d1=0;
            q1=i+1;
            break;
        }
        if (q1==-1) {
            memset(ok1,true,sizeof(ok1));
            int ss=lef[n-1];
            d1=1;
            do {
                ok1[ss+4]=false;
                foru(i,0,n) if (cal(ss,lef[i])==2) {
                    q1=i+1;
                    ss=2;
                    break;
                }
                if (ss==2) break;
                d1++;
                ss=cal(ss,lef[n-1]);
                if (ss==2) {
                    q1=0;
                    break;
                }
            } while (ok1[ss+4]);
        }
        int d2=0, q2=-1;
        ford(i,n-1,-1) if (rig[i]==4) {
            d2=0, q2=n-i;
            break;
        }
        if (q2==-1) {
            memset(ok2,true,sizeof(ok2));
            int ss=lef[n-1];
            d2=1;
            do {
                ok2[ss+4]=false;
                ford(i,n-1,-1) if (cal(rig[i],ss)==4) {
                    q2=n-i;
                    ss=4;
                    break;
                }
                if (ss==4) break;
                d2++;
                ss=cal(ss,lef[n-1]);
                if (ss==4) {
                    q2=0;
                    break;
                }
            } while (ok2[ss+4]);
        }
        if (q1==-1 || q2==-1 || q1+q2+(d1+d2)*n>n*m) printf("NO\n"); else printf("YES\n");
    }
    fclose(stdin);
    fclose(stdout);
    re 0;
}

