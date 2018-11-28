#include<cstdio>
#include<algorithm>
#include<iostream>
#include<vector>
#include<set>
#include<map>
#include<cmath>
#include<string>
#include<cstring>
#include<bitset>
#define pii pair<int,int>
#define A first
#define B second
using namespace std;
int T,tag[10],ct;
long long n,t,t2;
void Do(){
    scanf("%lld",&n);
    if(n == 0ll) printf("INSOMNIA");
    else{
        for(int i=0;i<10;i++) tag[i] = 0;
        ct = 0; t = 0ll;
        while(ct < 10){
            t += n;
            t2 = t;
            while(t2 > 0){
                if(tag[t2%10] == 0) tag[t2%10] = 1, ct++;
                t2 /= 10ll;
            }
        }
        printf("%lld",t);
    }
}
int main(){
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    for(int rr=1;rr<=T;rr++){
        printf("Case #%d: ",rr);
        Do();
        printf("\n");
    }
    return 0;
}
