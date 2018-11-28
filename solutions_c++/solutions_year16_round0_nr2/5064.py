#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<string>
#include<map>
#include<set>
#include<algorithm>
#define CLR(x) memset(x,0,sizeof(x))
#define REP(i,l,r) for(int i=l;i<=r;i++)
#define rep(i,l,r) for(int i=l;i<r;i++)
#define RREP(i,l,r) for(int i=l;i>=r;i--)
#define rrep(i,l,r) for(int i=l;i>r;i--)
#define _s(x) scanf("%d",&x)
#define _sc(x) scanf("%c",&x)
#define _ss(x) scanf(" %s",x)
#define _sl(x) scanf("%I64d",&x)
#define _sd(x) scanf("%lf",&x)
#define _pt(x) printf("%d",x)
#define _ps(x) printf("%s",x)
#define _pc(x) printf("%c",x)
#define _pd(x) printf("%f",x);
#define _pl(x) printf("%I64d",x)
#define _pn printf("\n");
#define _p printf(" ");
#define gch getchar()
#define debug(x) printf("%d\n",x)
#define ll long long

using namespace std;

int t,k;
char a[110];

void rev(int r){
   REP(i,0,r/2){
     swap(a[i],a[r-i]);
     a[i]=(a[i]=='+')?'-':'+';
     if(r-i!=i){
        a[r-i]=(a[r-i]=='+')?'-':'+';
     }
   }
}

int main(){
  freopen("B-large.in","r",stdin);
  freopen("B-large.out","w",stdout);
  _s(t);
  REP(i,1,t){
    _ss(a);
    printf("Case #%d: ",i);
    k=strlen(a);
    int l=0,r=k-1;
    bool flag=0;
    int num=0;
    while(r>=0){
       if(!flag){
          while(r>=0&&a[r]=='+') r--;
          if(r<0) break;
          if(a[0]=='+'){
            flag=1;
            num++;
            while(r>=0&&a[r]=='-') r--;
            if(r<0) break;
            rev(r);
          }else{
            rev(r);
          }
          num++;
       }else{
          while(r>=0&&a[r]=='-') r--;
          if(r<0) break;
          if(a[0]=='-'){
            flag=0;
            num++;
            while(r>=0&&a[r]=='+') r--;
            if(r<0) break;
            rev(r);
          }else{
            rev(r);
          }
          num++;
       }
    }
    _pt(num);_pn;
  }
}
