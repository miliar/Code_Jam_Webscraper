#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <utility>
#include <set>
#include <map>
#include <iostream>
#include <queue>
#include <cctype>

using namespace std;

typedef long long LL;

#define PB push_back
#define FRO freopen("in.txt","r",stdin);


#define SIZE 1000100

char str[SIZE];

bool isvowel( char &c ){
    return c=='a' || c=='e' ||c=='i' || c=='o' || c=='u';
}


int main(){

    freopen("A-small-attempt1.in","r",stdin);
    freopen("out.out","w",stdout);
    int kase,val;
    scanf("%d",&kase);

    for (int kk=1;kase--;++kk){
        scanf("%s %d",str,&val);
        printf("Case #%d: ",kk);
        int len=strlen(str);

        int cnt=0;
        int ans= 0;
        int prv= 0;
        for (int i=0;i<len;++i){
            if ( isvowel( str[i]) ){
                cnt=0;
            }else{
                cnt++;
                if ( cnt>= val ){
                    ans+=  (i-val+2-prv)*(len-i);
                    //printf("%d %d\n",(i-val+2-prv),(len-i));
                    prv= i-val+2;
                }
            }
        }
        printf("%d\n",ans);
    }

    return 0;
}
