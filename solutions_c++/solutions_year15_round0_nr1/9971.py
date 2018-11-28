#include<iostream>
#include<string>
#include<sstream>
#include<cstring>
#include<stack>
#include<math.h>
#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<limits.h>
#include<algorithm>
#include<cstdio>
#include<map>
#include<memory>
#include<iomanip>
#include<string>
#include<istream>
#include<wchar.h>
#include<vector>
#include<cstdlib>
#include<cmath>
#include<ctime>
#include<stack>
#include<queue>
#include<fstream>
#include<ostream>
using namespace std;

#define sd(a) scanf("%d",&a)
#define sl(a) scanf("%ld",&a)
#define sll(a) scanf("%lld",&a)
#define sc(a) printf("%c",&a)
#define pd(a) printf("%d ",a)
#define pl(a) printf("%ld ",a)
#define pll(a) printf("%lld ",a)
#define pc(a) printf("%c",a)
#define pf(a) printf("%s",a);
#define f(i,n) for(i=0;i<n;i++)
#define flu(i,l,u) for(i=l;i<u;i++)
#define max(a,b) a>b?a:b
#define ssout(a) std::cout<<a
#define ssin(a) std::cin>>a
#define max(a,b) a>b?a:b
#define min(a,b) a>b?b:a


int main()
{
    int i=0,j=0,k=0;
    int T=0,smax=0,totaud=0,ans=0;
    sd(T);
    char *str;
    for(i=1;i<=T;i++){
        ans=0;
        sd(smax);
        str = new char[smax+1];
        ssin(str);
        totaud = str[0]-48;
        for(j=1;j<smax+1;j++){
            if(j>totaud){
                ans+=j-totaud;
                totaud=j;
            }
                totaud += str[j]-48;
            
        }
        //cout<<"Case #"<<i<<": "<<str<<"\n";
        cout<<"Case #"<<i<<": "<<ans<<"\n";
        delete str;
    }
    return 0;
}
