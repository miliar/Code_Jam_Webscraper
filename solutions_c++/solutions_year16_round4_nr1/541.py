#include <iostream>
#include <iomanip>
#include <fstream>
#include <stdlib.h>
#include <time.h>
#include<cstring>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include <limits.h>
#include<cmath>
#include<map>
#include<queue>
#include<set>
using namespace std;

#define N 100005
#define M 100005
#define LL long long

//为自己加油O(∩_∩)O~

const long long  mod =1000000007;
string z,x;
string g,h;
void er(int n)
{
    for (int j=1;j<=n;j++){
        int len=1<<j;
        for (int k=0;k*len<z.size();k++){
            g=z.substr(k*len,len/2);
            h=z.substr(k*len+len/2,len/2);
            if (g>h){
                for (int l=k*len,f=0;f<len;f++,l++){
                    if (f>=len/2) z[l]=g[f-len/2];else z[l]=h[f];
                }
            }
        }
    }
}
int main()
{
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    int t=T;
    while (T--){
        int n,r,p,s;
        scanf("%d%d%d%d",&n,&r,&p,&s);
        int nr=r,np=p,ns=s;
        bool b=true;
        for (int j=0;j<n;j++){
            int sum=r+p+s;
            sum/=2;
            ns=sum-r;
            nr=sum-p;
            np=sum-s;
            if (nr<0 || np<0 || ns<0) {
                b=false;break;
            }
            if (j+1!=n) {r=nr;p=np;s=ns;}
        }
        if (!b){
            printf("Case #%d: IMPOSSIBLE\n",t-T);
            continue;
        }
        if (r==p && r==1) z="PR";
        if (r==s && s==1) z="RS";
        if (s==p && s==1) z="PS";
        for (int j=1;j<n;j++){
            x="";
            int q0=0,q1=0,q2=0;
            for (int k=0;k<z.size();k++){
                if (z[k]=='P') x+="PR";
                if (z[k]=='R') x+="RS";
                if (z[k]=='S') x+="PS";
                //cout<<x<<endl;
            }
//            for (int k=0;k<q0;k++) x+="PR";
//            for (int k=0;k<q1;k++) x+="PS";
//            for (int k=0;k<q2;k++) x+="RS";
            z=x;
        }
        er(n);
        printf("Case #%d: ",t-T);
        cout<<z<<endl;
    }
    return 0;
}








