/* 1352652 周宇星 数理强化班 */
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
#include <cassert>
using namespace std;

/*
int get(){
  char c;
  while(c=getchar(),(c<'0'||c>'9')&&(c!='-'));
  bool flag=(c=='-');
  if(flag) c=getchar();
  int x=0;
  while(c>='0'&&c<='9'){
      x=x*10+c-48;
      c=getchar();
  }
  return flag?-x:x;
}
void output(int x){
  if(x<0){
      putchar('-');
      x=-x;
  }
  int len=0,data[10];
  while(x){
      data[len++]=x%10;
      x/=10;
  }
  if(!len) data[len++]=0;
  while(len--) putchar(data[len]+48);116.5.12.148
  putchar('\n');
}*/


/*----------------------------------------------Thanks for viewing--------------------------------*/

const int N = 5, g[N][N]={{0,0,0,0,0},
                          {0,1,2,3,4},
                          {0,2,-1,4,-3},
                          {0,3,-4,-1,2},
                          {0,4,3,-2,-1}},
                 s[N][N]={{0,1,1,1,1},
                          {0,1,-1,1,-1},
                          {0,1,-1,-1,1},
                          {0,1,1,-1,-1}},
                inv[N]  ={0,1,-2,-3,-4};
const int maxl =10025;
int T,X,L,n;
char a[maxl];
int m1[maxl],m2[maxl];
vector<int> p1,p2;

int sgn(int x) {
    return x<0?-1:1;
}

int abs(int x) {
    return x<0?-x:x;
}


int mul(int x,int y){
    return sgn(x)*sgn(y)*g[abs(x)][abs(y)];
}

void pre1() {
    int c=1;
    for(int i = 0; i < n;i++) {
        c=mul(c,a[i]);
        m1[i]=c;
        if(c==2)
            p1.push_back(i);
    }
}

void pre2() {
    int c=1;
    for(int i = n-1; i >= 0;i--) {
        c=mul(a[i],c);
        m2[i]=c;
        if(c==4)
            p2.push_back(i);
    }
}

bool check(int l, int r) {
    int x=m1[l-1], y=m1[r], invx=sgn(x)*inv[abs(x)], v=mul(invx,y);
    return v==3;
}

int main() {
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);
    scanf("%d",&T);
    for(int t0=1;t0<=T;t0++){
        memset(a,0,sizeof(a));
        p1.clear();
        p2.clear();
        scanf("%d%d",&L,&X);
        n=L*X;
        scanf("%s",a);
        for(int i=0;a[i];i++)
            a[i]=a[i]-'i'+2;
        int p=L;
        for(int i=1;i<X;i++)
            for(int j=0;j<L;j++)
                a[p++]=a[j];
        pre1();
        pre2();
        bool ok=false;
        for(int i = 0; i < p1.size(); i++)
            for(int j = 0; j < p2.size(); j++)
                if(p1[i]<p2[j]-1){
                    if(check(p1[i]+1,p2[j]-1)){
                        ok = true;
                        goto print;
                    }
                }
                else{
                    break;
                }
        print:
        if(ok)
            printf("Case #%d: YES\n",t0);
        else
            printf("Case #%d: NO\n",t0);
    }
}

