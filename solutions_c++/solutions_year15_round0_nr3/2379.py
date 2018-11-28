#include<bits/stdc++.h>
#define LL long long
#define MAXL 10005
#define f_in(st) freopen(st,"r",stdin);
#define f_out(st) freopen(st,"w",stdout);
using namespace std;

LL results[5][5] = {
    {0, 0, 0, 0, 0},
    {0, 1, 2, 3, 4},
    {0, 2, -1, 4, -3},
    {0, 3, -4, -1, 2},
    {0, 4, 3, -2, -1}
};

LL convert(char c)
{
if(c==1)return c-'0';
else return c-'i'+2;
}

LL multiply(LL a,LL b)
{
    LL ans=1;
    if(a<0){
            ans*=-1;
            a*=-1;
    }
    if(b<0){
      ans*=-1;
      b*=-1;
    }
    LL ret=results[a][b];
    return ret*ans;
}
LL findPrefix(LL,LL,LL);
LL findSuffix(LL,LL,LL);
LL product_left[MAXL],product_right[MAXL],val[MAXL];

int main(){
    f_in("in2.txt");
    f_out("out.txt");
    LL T;
    cin>>T;
    for (LL testCase = 1; testCase <= T; testCase++)
    {
        cout << "Case #" << testCase << ": ";
      LL L,X;
      cin>>L>>X;
      string s;
      cin>>s;
      val[0]=convert(s[0]);
      product_left[0]=val[0];
      for(LL i=1;i<L;i++)
      {
          val[i]=convert(s[i]);
          product_left[i]=multiply(product_left[i-1],val[i]);
      }
      product_right[L-1]=convert(s[L-1]);
      for(LL i=L-2;i>=0;i--)
      {
          product_right[i]=multiply(product_right[i+1],val[i]);
      }
      LL all = product_left[L-1];
      LL prodAll = 1;
      LL Modpow = X%4;
        for(LL i=0;i<Modpow;i++)
         prodAll=multiply(prodAll,all);
        if (prodAll!=-1){
            printf("NO\n");
            continue;
        }
        LL prefix = -1;
        LL times=findPrefix(1,all,2);
        if (times>0){
            prefix=L*times;
        }
        for(LL i=0;i<L;i++){
            LL v=product_left[i];
            LL times = findPrefix(v, all, 2);
            if (times < 0) continue;
            LL len = i + 1 + L * times;
            if (prefix<0||len<prefix)
            prefix=len;
        }
        LL suffix = -1;
        times = findSuffix(1, all, 4);
        if (times > 0) {
            suffix=L*times;
        }
        for(LL i=0;i<L;i++){
            LL v = product_right[i];
            LL times = findSuffix(v, all, 4);
            if (times < 0) continue;
            LL len = L-i+L*times;
            if (suffix<0 || len<suffix)
                suffix=len;
        }


        if (prefix < 0 || suffix < 0) {
         printf("NO\n");
         continue;
        }
        LL totalLen = L * X;
        LL reqLen = prefix + suffix;
        if (reqLen >= totalLen) {
            printf("NO\n");
            continue;
        }
        printf("YES\n");
    }
    return 0;
}

LL findPrefix(LL pre,LL all,LL req) {
    if (pre == req) return 0;
    LL allPow = all;
    for(LL i=1;i<4;i++){
        LL val = multiply(allPow, pre);
        allPow = multiply(allPow, all);
        if (val == req) return i;
    }
    return -1;
}

LL findSuffix(LL suf,LL all,LL req) {
    if (suf == req) return 0;
    LL allPow = all;
    for(LL i=1;i<4;i++) {
        LL val = multiply(suf, allPow);
        allPow = multiply(all, allPow);
        if (val == req) return i;
    }
    return -1;
}
