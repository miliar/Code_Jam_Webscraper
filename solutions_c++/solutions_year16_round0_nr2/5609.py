#include<bits/stdc++.h>
using namespace std;
#define lli long long int
int main()
{
    lli testcase;
    char sandeep[111];
    scanf("%lld" , &testcase);
    lli i;
    for(i=1 ; i<=testcase ; ++i)
        {
         lli ans = 0;
        scanf("%s" , sandeep);
        lli l = strlen(sandeep);
        while(l--){
            if(sandeep[l]=='-'){
              ans++;
              for(lli j=0 ;j<=l ; ++j){
                if(sandeep[j]=='-')
                    sandeep[j] = '+';
                else
                    sandeep[j] = '-';
              }
            }
        }
        printf("Case #%lld: %lld\n" , i , ans);
    }
    return 0;
}
