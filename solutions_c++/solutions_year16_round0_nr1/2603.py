#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
bool bucket[15];
void mark(ll x){
    while (x>0){
        int m=x%10;
        bucket[m]=true;
        x/=10;
    }
}
bool check(){
    for (int i=0; i<=9; i++){
        if (!bucket[i]) return false;
    }
    return true;
}
void _clear(){
    for (int i=0; i<=9; i++) bucket[i]=false;
}
int main()
{
    int t;
    ll n,c,aux;

    freopen("A-large.in","r",stdin);
    freopen("A-large_output.out","w",stdout);

    scanf("%d",&t);
    for (int _case=1; _case<=t; _case++){
        scanf("%lld",&n);
        if (n==0){
            printf("Case #%d: INSOMNIA\n",_case);
            continue;
        }
        c=1;
        while (!check()){
            aux=c*n; c++;
            mark(aux);
        }
        printf("Case #%d: %lld\n",_case,aux);
        _clear();
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
