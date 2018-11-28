#include <bits/stdc++.h>
using namespace std;
typedef long long int lli;
set<lli> S;
void hashDigits(lli n){
    while(n){
        S.insert(n%10);
        n/=10;
    }
}
bool done(){
    if(S.size() == 10) return true;
    else return false;
}
int main(){
    int t;
    lli n;
    scanf("%d",&t);
    for(int q = 0;q<t;q++){
        S.clear();
        printf("Case #%d: ",q+1);
        cin>>n;
        if(n == 0){
            printf("INSOMNIA\n");
        }else{
            lli val = n;
            while(!done()){
                hashDigits(val);
                if(done()){
                    printf("%lld\n",val);
                    break;
                }
                val += n;
            }
        }
    }
    return 0;
}