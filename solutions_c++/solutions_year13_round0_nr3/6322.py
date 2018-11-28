#include<algorithm>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<fstream>
#include<iostream>
#include<map>
#include<vector>
using namespace std;

int d[100];

bool cp(int n) {
     int i,x=n,a=0,j;
     while(x>0) {
                d[a]=x%10;
                x/=10;
                ++a;
     }
     for(i=0,j=a-1;i<j;++i,--j) if(d[i]!=d[j]) break;
     if(i<j) return 0;
     return 1;
}

int main() {
    freopen("C.in","rt",stdin);
    freopen("C.out","wt",stdout);
    int t,c,a,b,i,s,r;
    scanf("%d",&t);
    for(c=0;c<t;++c) {
                     scanf("%d %d",&a,&b);
                     r=0;
                     for(i=a;i<=b;++i) {
                                       if(fmod(sqrt(i),1.0)==0.0) break;
                     }
                     if(i<=b) {
                              s=sqrt(i);
                              for(;s*s<=b;++s) {
                                               if(cp(s)) if(cp(s*s)) ++r;
                              }
                     }
                     printf("Case #%d: %d\n",c+1,r);
    }
    //system("pause");
}
