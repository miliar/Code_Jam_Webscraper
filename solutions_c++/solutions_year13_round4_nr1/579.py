#include<cmath>
#include<cstdio>
#include<cctype>
#include<vector>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>
using namespace std;

#define sqr(a) (a)*(a)
#define cub(a) (a)*(a)*(a)
#define for1(i,a,b) for(i=(a);i<(b);i++)
#define for2(i,a,b) for(i=(a);i>(b);i--)
#define same(a) memset((a),0,sizeof(a));
#define ll long long

const int MOD = 1000000009;

int cmpint(const void*a,const void *b)
{
    if(((int*)a)[0]==((int*)b)[0])
      return ((int*)a)[1]-((int*)b)[1];
    return ((int*)a)[0]-((int*)b)[0];
}

int a[100005][3];
int b[100005][2];

int c[100005][2];

int main()
{
    int i,j,n,m,k,l,o,p;
    int ans;
    ll tmp;
    ll AN;
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    scanf("%d",&p);
    for1(o,1,p+1){
        scanf("%d%d",&n,&m);
        AN=n;
        same(a);
        same(b);
        same(c);
        for1(i,0,m)
         for1(j,0,3)
          scanf("%d",&a[i][j]);
        ans=0;
        qsort(a,m,sizeof(int)*3,cmpint);
        int ans1=0;
        for1(i,0,m){
            k=a[i][1]-a[i][0];
            tmp=(AN+AN-k+1)*k/2%1000002013;
            tmp=tmp*a[i][2]%1000002013;
            ans1+=tmp;
            ans1%=1000002013;
        }
        for1(i,0,m){
            b[i*2][0]=a[i][0];
            b[i*2][1]=a[i][2];
            b[i*2+1][0]=a[i][1];
            b[i*2+1][1]=-a[i][2];
        }
        m*=2;
        qsort(b,m,sizeof(int)*2,cmpint);
        for2(i,m-1,0)
          if(b[i][0]==b[i-1][0]){
              b[i-1][1]+=b[i][1];
              b[i][1]=0;
          }
        qsort(b,m,sizeof(int)*2,cmpint);
       // for1(i,0,m) printf("%d %d\n",b[i][0],b[i][1]);
        k=0;
        for1(i,0,m)
            if(b[i][1]!=0){
                if(b[i][1]>0){
                    c[k][0]=b[i][0];
                    c[k][1]=b[i][1];
                    k++;
                }
                else{
                   // printf("%d %d %d\n",k,c[k-1][0],c[k-1][1]);
                    while(b[i][1]!=0){
                        if(b[i][1]+c[k-1][1]<=0){
                            l=b[i][0]-c[k-1][0];
                            tmp=(AN+AN-l+1)*l/2%1000002013;
                            tmp=tmp*c[k-1][1]%1000002013;
                            ans=(ans+tmp)%1000002013;
                            b[i][1]+=c[k-1][1];
                            c[k-1][1]=0;
                            k--;

                        }
                        else{
                            l=b[i][0]-c[k-1][0];
                            tmp=(AN+AN-l+1)*l/2%1000002013;
                            tmp=tmp*(-b[i][1])%1000002013;
                            ans=(ans+tmp)%1000002013;
                            c[k-1][1]+=b[i][1];
                            b[i][1]=0;
                        }
                       // system("pause");
                    }
                }
            }
        //printf("%d %d\n",ans1,ans);
        ans=ans1-ans;
        if(ans<0) ans+=1000002013;
        printf("Case #%d: %d\n",o,ans);
    }
    return 0;
}
