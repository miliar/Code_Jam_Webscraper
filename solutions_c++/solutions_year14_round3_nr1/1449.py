#include <cstdio>
#include <iostream>
#include <cmath>
#include <climits>
#include <utility>
#include <algorithm>
#include <vector>
#include <map>
#include <string.h>
using namespace std;
long long gcd(long long a,long long b){
    if(a%b==0) return b;
    return gcd(b,a%b);
}
int main(){
    freopen("a.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int uu=0;uu<t;uu++){
        long long p,q;
        char ch;

        scanf("%lld%c%lld",&p,&ch,&q);
        long long g = gcd(q,p);
        p = p/g;
        q = q/g;
        //cout << p << " " << ch << " " << q << endl;
        if((q&(-q))!=q){
            printf("Case #%d: impossible\n",uu+1);
        }
        else{
            q = q>>1;
            int count = 1;
            while(p<q && q>0){
                q = q>>1;
                count++;
            }
            printf("Case #%d: %d\n",uu+1,count);
        }
    }
    return 0;
}
