#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<string>
#include<vector>
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
#define pb push_back
#define ll long long

using namespace std;

int t;
char a[3000];

int N[30];
int ord[10]={0,2,6,8,7,3,4,5,9,1};
int res[20];

bool check(){
   rep(i,0,26){
     if(N[i]>0){
        return 0;
     }
   }
   return 1;
}

int trans(char z){
  return z-'A';
}

bool hasNum(int n){
   if(n==0){
      return N[trans('Z')]&&N[trans('E')]&&N[trans('R')]&&N[trans('O')];
   }
   if(n==1){
      return N[trans('O')]&&N[trans('N')]&&N[trans('E')];
   }
   if(n==2){
      return N[trans('T')]&&N[trans('W')]&&N[trans('O')];
   }
   if(n==3){
      return N[trans('T')]&&N[trans('H')]&&N[trans('R')]&&N[trans('E')]>=2;
   }
   if(n==4){
      return N[trans('F')]&&N[trans('O')]&&N[trans('U')]&&N[trans('R')];
   }
   if(n==5){
      return N[trans('F')]&&N[trans('I')]&&N[trans('V')]&&N[trans('E')];
   }
   if(n==6){
      return N[trans('S')]&&N[trans('I')]&&N[trans('X')];
   }
   if(n==7){
      return N[trans('S')]&&N[trans('E')]>=2&&N[trans('V')]&&N[trans('N')];
   }
   if(n==8){
      return N[trans('E')]&&N[trans('I')]&&N[trans('G')]&&N[trans('H')]&&N[trans('T')];
   }
   if(n==9){
      return N[trans('N')]>=2&&N[trans('I')]&&N[trans('E')];
   }

}

void solve(int n){
   if(n==0){
      N[trans('Z')]--;
      N[trans('E')]--;
      N[trans('R')]--;
      N[trans('O')]--;
   }
   if(n==1){
      N[trans('O')]--;
      N[trans('N')]--;
      N[trans('E')]--;
   }
   if(n==2){
      N[trans('T')]--;
      N[trans('W')]--;
      N[trans('O')]--;
   }
   if(n==3){
      N[trans('T')]--;
      N[trans('H')]--;
      N[trans('R')]--;
      N[trans('E')]-=2;
   }
   if(n==4){
      N[trans('F')]--;
      N[trans('O')]--;
      N[trans('U')]--;
      N[trans('R')]--;
   }
   if(n==5){
      N[trans('F')]--;
      N[trans('I')]--;
      N[trans('V')]--;
      N[trans('E')]--;
   }
   if(n==6){
      N[trans('S')]--;
      N[trans('I')]--;
      N[trans('X')]--;
   }
   if(n==7){
      N[trans('S')]--;
      N[trans('E')]-=2;
      N[trans('V')]--;
      N[trans('N')]--;
   }
   if(n==8){
      N[trans('E')]--;
      N[trans('I')]--;
      N[trans('G')]--;
      N[trans('H')]--;
      N[trans('T')]--;
   }
   if(n==9){
      N[trans('N')]-=2;
      N[trans('I')]--;
      N[trans('E')]--;
   }

}

int main(){
   freopen("A-large.in","r",stdin);
   freopen("A-large.out","w",stdout);
   _s(t);
   REP(cas,1,t){
       _ss(a);
       printf("Case #%d: ",cas);
       int k=strlen(a);
       CLR(N);CLR(res);
       rep(i,0,k){
         N[a[i]-'A']++;
       }
       REP(i,0,9){
         while(hasNum(ord[i])){
            solve(ord[i]);
            res[ord[i]]++;
         }
       }
       REP(i,0,9){
         REP(j,1,res[i]){
            printf("%d",i);
         }
       }
       _pn;
   }
}
